from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from adktools import discover_adk_tools

AGENT_MODEL = "openai/gpt-4o-mini"

trip_tailor_agent = Agent(
    name="trip_tailor_agent",
    model=LiteLlm(model=AGENT_MODEL),
    description="Creates travel itineraries based on location and travel dates",
    instruction=(
        "You are TripTailor, a helpful travel assistant. Your goal is to create simple, budget-friendly travel itineraries "
        "for users based on their chosen location and travel dates. "
        "When the user provides these details, you have to use the 'get_places' tool to gather attractions or activities, "
        "and the 'get_weather' tool to get weather forecasts for the given dates. "
        "Combine these results into a clear, day-by-day itinerary. "
        "If tools fail or return errors, politely inform the user and provide alternative suggestions."
    ),
    #tools=discover_adk_tools(trip_tailor.tools)
)
