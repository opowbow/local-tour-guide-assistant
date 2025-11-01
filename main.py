import os
import logging
import asyncio
import uuid
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

from coordinator.agent import root_agent as trip_planner_agent, tour_guide_coordinator
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("local_explorer_assistant_api")
logger.setLevel(logging.INFO)

APP_NAME = "local-explorer-assistant"
USER_ID = os.getenv("USER_ID", "user")
SESSION_ID = str(uuid.uuid4())


app = FastAPI()

# Define a new input model for location data
class LocationData(BaseModel):
    latitude: float
    longitude: float

@app.post("/discover-location")
async def discover_location(location: LocationData):
    """
    This endpoint receives a user's location, identifies the nearby landmark,
    and returns interesting facts about it as text and audio.
    """
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )
    runner = Runner(
        agent=tour_guide_coordinator,
        app_name=APP_NAME,
        session_service=session_service,
    )
    # The user's query will be the location data
    user_query = f"Tell me about the building at latitude {location.latitude}, longitude {location.longitude}"
    
    # Send the query to the coordinator agent
    # The coordinator will handle the new workflow
    content = Content(role="user", parts=[Part(text=user_query)])

    response_text = ""
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=content
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                response_text += event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            break

    # Generate audio from the response text
    # This uses the `generate_audio` tool I have access to.
    # audio_url = generate_audio(response_text) 
    
    return {
        "text_summary": response_text,
        # "audio_summary_url": audio_url
    }
runner: Runner = None

class TripRequest(BaseModel):
    location: str
    interests: List[str]
    duration_hours: float
    avoid: Optional[List[str]] = []

@app.on_event("startup")
async def init_runner():
    """
    Init runner
    Args:  
        None
    Returns:
        None
    """
    global runner
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )
    runner = Runner(
        agent=trip_planner_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )
    logger.info("Runner initialized and session created.")

@app.post("/plan")
async def plan_trip(request: TripRequest):
    """
        Plan trip
    Args:
        request (TripRequest): request with the location, duration (in hours)
            interests (e.g. sport, art, history), and avoid (e.g. crowds, noise)
    Returns:
        itinerary (str): Markdown formated text with the itinerary description
    """
    global runner
    user_input = (
        f"I will be in {request.location} for {request.duration_hours} hours. "
        f"I'm interested in {', '.join(request.interests)}. "
        f"Please avoid: {', '.join(request.avoid or [])}."
    )
    logger.info(f"User input: {user_input}")
    content = Content(role="user", parts=[Part(text=user_input)])

    response_text = ""
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=content
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                response_text += event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            break
    logger.info("System response: {response_text}")
    return {"itinerary": response_text}
