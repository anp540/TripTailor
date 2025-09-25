import pytest
from models import TripRequest, Itinerary, ItineraryDay

def test_trip_request():
    req = TripRequest(location="Paris, France", start_date="2025-09-24", end_date="2025-09-30")
    assert req.location == "Paris, France"
    assert req.start_date == "2025-09-24"
    assert req.end_date == "2025-09-30"

def test_itinerary_day():
    day = ItineraryDay(date="2025-09-25", activities=["Eiffel Tower", "Louvre"], notes="Sunny day")
    assert day.date == "2025-09-25"
    assert "Eiffel Tower" in day.activities
    assert day.notes == "Sunny day"

def test_itinerary():
    days = [ItineraryDay(date="2025-09-25", activities=["Eiffel Tower"]) ]
    itin = Itinerary(location="Paris, France", start_date="2025-09-24", end_date="2025-09-30", days=days)
    assert itin.location == "Paris, France"
    assert itin.days[0].activities[0] == "Eiffel Tower"
