from adk.api.agents import Agent
from adk.api.tools import Tool, tool

class IdentifierAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            description="Identifies a landmark or building from GPS coordinates using Google Maps.",
            # The native google_maps_grounding tool is perfect for this
            tools=[google_maps_grounding] 
        )

    @tool(name="IdentifyPlaceFromLocation")
    def identify_place(self, latitude: float, longitude: float) -> str:
        """
        Takes latitude and longitude and returns the name of the place.
        It uses the google_maps_grounding tool to find nearby places of interest.
        """
        # The prompt will instruct the model to use the grounding tool
        # to find the most prominent landmark at these coordinates.
        prompt = f"What is the name of the most prominent building or landmark at latitude {latitude}, longitude {longitude}?"
        
        # This will invoke the LLM with the Maps tool to find the place name.
        place_name = self.query(prompt)
        return place_name
