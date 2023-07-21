class BookingLandingPage:
    def __init__(self, p_driver):
        self.driver = p_driver
        self.driver.get("https://www.booking.com/")

    def set_destination(self, destination):
        # Set destination
        # Click on the "Destination" field
        # Click on the "Done" button
        pass

    def set_time_frame(self, departure_date, return_date):
        # Set time frame for travel
        # Click on the "Departure" field
        # Click on the "Return" field
        # Click on the "Done" button
        pass

    def set_passengers_and_rooms(self, adults, children, rooms):
        # Set number of passengers
        # Click on the "Passengers" field
        # Click on the "Adults" field
        # Click on the "Done" button
        pass

    def start_search(self):
        # Click on the "Search" button
        # Wait for the search results page to load
        pass
