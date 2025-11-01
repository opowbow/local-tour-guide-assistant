from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from subagents.discovery import discovery_agent
from subagents.routing import routing_agent
from subagents.composer import composer_agent
from subagents.identifier import identifier_agent

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

tour_guide_instruction_prompt = """
You are a tour guide coordinator. Your goal is to provide interesting facts about a landmark at a given location.
You have access to the following tools:
- `identifier_agent`: to identify the landmark at the given GPS coordinates.
- `discovery_agent`: to find interesting facts about the identified landmark.
- `composer_agent`: to create a friendly and engaging narrative from the facts.

Here's the workflow:
1. Use the `identifier_agent` to find the name of the landmark from the user's location (latitude and longitude).
2. Once you have the landmark name, use the `discovery_agent` to search for interesting facts about it.
3. Finally, use the `composer_agent` to generate a script with the information found.

Do not ask the user for clarification. Allways offer one option for the local exploration, do not create a conversational experience.
"""

tour_guide_coordinator = Agent(
    name="tour_guide_coordinator",
    model="gemini-2.5-pro",
    description="Orchestrates the identifier, discovery, and composer agents to provide tour guide information.",
    instruction=tour_guide_instruction_prompt,
    tools=[
        AgentTool(agent=identifier_agent),
        AgentTool(agent=discovery_agent),
        AgentTool(agent=composer_agent)
    ]
)
