from google.adk.agents import Agent
import os
import logging
import requests

from dotenv import load_dotenv

load_dotenv()



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def maps_search_route(start: str, end: str, waypoints: list):
    """
    Search route using Google Maps Directions API
    Args:
        start (str): starting point
        end (str): end point
        waypoints (list): list of points on the path
    Returns:
        data (dict): the route data
    """
    try:
        GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={end}&waypoints={'|'.join(waypoints)}&mode=walking&key={GOOGLE_MAPS_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logger.debug(f"Google Maps API Response: {data}")
        return data
    except requests.exceptions.HTTPError as err:
        logger.error(f"HTTP error occurred: {err}")
    except Exception as err:
        logger.error(f"Other error occurred: {err}")

instruction_prompt = """
You are a routing agent. Use the maps_search_route tool to estimate the best route and travel times between a start and destination with optional waypoints.
You can use the tool: maps_search_route.
This tool is already configured to use:
    start (str): the starting point
    end (str): the ending point
    waypoints (list): the list of landmarks/locations
The tool is already configured to use walking only.
Use it accordingly.
"""

routing_agent = Agent(
    name="routing_agent",
    model="gemini-2.5-pro",
    description="Estimates an optimal travel route using Google Maps Directions API. through `maps_search_route` tool",
    instruction=instruction_prompt,
    tools=[maps_search_route]
)