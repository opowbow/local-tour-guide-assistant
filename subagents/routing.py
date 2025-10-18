import logging

from google.adk.agents import Agent
from google.adk.tools import google_maps_grounding

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


instruction_prompt = """
    You are a routing agent. Use the google_maps_grounding tool to estimate the best route and travel times 
    between a start and destination with optional waypoints.
    You can use the tool: google_maps_grounding.
    Walking is preferable but local transportation is also acceptable, if available.
"""

routing_agent = Agent(
    name="routing_agent",
    model="gemini-2.5-pro",
    description=(
        "Estimates an optimal travel route using ADK v1.15+ google_maps_grounding tool."
    ),
    tools=[google_maps_grounding],
)