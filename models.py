from pydantic import BaseModel, Field
from typing import List, Optional
from adktools.models import DomainError


class TripRequest(BaseModel):
    location: str = Field(..., description="City or location for the trip (e.g., 'Paris, France').")
    start_date: str = Field(..., description="Start date of the trip in YYYY-MM-DD format.")
    end_date: str = Field(..., description="End date of the trip in YYYY-MM-DD format.")


class ItineraryDay(BaseModel):
    date: str = Field(..., description="The date for this day in the itinerary.")
    activities: List[str] = Field(..., description="List of planned activities for the day.")
    notes: Optional[str] = Field(None, description="Optional notes for the day (e.g., weather or tips).")


class Itinerary(BaseModel):
    location: str = Field(..., description="Trip location.")
    start_date: str = Field(..., description="Trip start date.")
    end_date: str = Field(..., description="Trip end date.")
    days: List[ItineraryDay] = Field(..., description="List of days with activities.")


class InvalidTripRequestError(DomainError):
    """Error when the trip request input is invalid."""
    details: str = Field(..., description="Details about why the request is invalid.")
