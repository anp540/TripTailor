# trip_tailor/agent.py
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Import tools
import trip_tailor.tools
from adktools import discover_adk_tools

# Set the LLM model
AGENT_MODEL = "openai/gpt-4o-mini"

# Root agent for TripTailor
trip_tailor_agent = Agent(
    name="trip_tailor_agent",
    model=LiteLlm(model=AGENT_MODEL),
    description="Creates travel itineraries based on location, travel dates, and budget.",
    instruction=(
        "You are TripTailor, a helpful travel assistant. Your goal is to create simple, budget-friendly travel itineraries "
        "for users based on their chosen location, travel dates, and budget. "
        "When the user provides these details, you MUST use the 'get_places' tool to gather attractions or activities, "
        "and the 'get_weather' tool to get weather forecasts for the given dates. "
        "Combine these results into a clear, day-by-day itinerary. "
        "If tools fail or return errors, politely inform the user and provide alternative suggestions."
    ),
    tools=discover_adk_tools(trip_tailor.tools)
)
