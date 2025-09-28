from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from subagents.discovery import discovery_agent
from subagents.routing import routing_agent
from subagents.composer import composer_agent

instruction_prompt = """
You are a travel coordinator agent that creates a personalized itinerary for a traveler based on their interests and available time.
Ypu have access to three Agent Tools:
    - discovery_agent
    - routing_agent
    - composer_agent

- Use `discovery_agent` to find relevant places. 
    This would be the first action typically.
- Use `routing_agent` to plan the optimal route between those places.
    Use this tool once you decided on a number of places to visit.
- Use `composer_agent` to convert the raw route and POIs into a clear, human-readable itinerary. 
    Use preferably markdown notation.
- Do not ask user for further clarifications. Just propose the attractions, route, adding 
hour information and distances, if you have these informations.
- Allways offer one option for the local exploration, do not create a conversational experience.
- Do not ask the user for confirmation before calling the tools.

"""

root_agent = Agent(
    name="local_explorer_assistant",
    model="gemini-2.5-pro",
    description="Coordinates discovery, routing, and itinerary composition to plan a smart local day trip.",
    instruction=instruction_prompt,
    tools=[
        AgentTool(agent=discovery_agent),
        AgentTool(agent=routing_agent),
        AgentTool(agent=composer_agent)
    ]
)
