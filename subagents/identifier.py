from google.adk.agents import Agent
from google.adk.tools import google_search

instruction_prompt = """
You are an identifier agent. Your job is to identify the landmark or building at the given GPS coordinates.
You will be given a latitude and longitude, and you need to return the name of the most prominent landmark at that location.
Use the google_search tool to find the name of the landmark.
"""

identifier_agent = Agent(
    name="identifier_agent",
    model="gemini-2.5-pro",
    description="Identifies a landmark or building from GPS coordinates using Google Search.",
    instruction=instruction_prompt,
    tools=[google_search]
)
