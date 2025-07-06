from google.adk.agents import Agent
from google.adk.tools import google_search

instruction_prompt = """
You are a travel discovery agent. Use Google Search to find the most relevant places and activities for a tourist,
based on given location and interests. Return a short list or paragraph.
Note: this list will be used further by the routing Agent.
"""

discovery_agent = Agent(
    name="discovery_agent",
    model="gemini-2.5-pro",
    description="Uses Google Search to discover relevant places.",
    instruction=instruction_prompt,
    tools=[google_search]
)
