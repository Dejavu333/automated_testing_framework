import time
import pytest
from testing_framework.pages.geci import BookingLandingPage

from setup import setup


class TestSearchFlights:
    def test_search_flights(self, p_driver=setup()):
        landing_page = BookingLandingPage(p_driver)
        time.sleep(20)


testObj = TestSearchFlights()
testObj.test_search_flights()
