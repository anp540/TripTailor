from models import TripRequest, Itinerary, ItineraryDay
from datetime import datetime


def main():
    print("Welcome to TripTailor!")
    location = input("Enter trip location: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    trip = TripRequest(location=location, start_date=start_date, end_date=end_date)
    print(f"\nTrip created: {trip}")

if __name__ == "__main__":
    main()
