"""Module provides a way to test the methods used in HotelList class."""
import unittest
from hotels import HotelList

all_hotels = HotelList()


# Working tests
class TestHotel(unittest.TestCase):
    """Class tests all working methods in the hotel class"""
    def test_hotel_creation(self):
        """Tests the hotel creation method"""
        self.assertEqual(all_hotels.create_hotel(2, "LeFang"), {
                        'HOTEL_ID': 2,
                        'HOTEL_NAME': 'LeFang',
                        'RESERVED_ROOMS': []})
        self.assertEqual(all_hotels.create_hotel(1, "Four stories"), {
                        'HOTEL_ID': 1,
                        'HOTEL_NAME': 'Four stories',
                        'RESERVED_ROOMS': []})

    def test_hotel_deletion(self):
        """Tests the hotel deletion method"""
        self.assertNotIn(all_hotels.delete_hotel(2, "LeFang"), {
                        'HOTEL_ID': 2,
                        'HOTEL_NAME': 'LeFang',
                        'RESERVED_ROOMS': []})

    def test_hotel_information(self):
        """Tests the hotel information display method"""
        self.assertEqual(all_hotels.display_hotel_info(1, "Four stories"),
                         ("Hotel found: Four stories"
                          " With the ID: 1"
                          " Reserved rooms: []"))

    def test_hotel_room_creation(self):
        """Tests the hotel room creation method"""
        self.assertEqual(
            all_hotels.create_room_reservation(1, "Four stories", 102),
            ([102]))

    def test_hotel_room_deletion(self):
        """Tests the hotel room deletion method"""
        self.assertEqual(
            all_hotels.cancel_room_reservation(1, "Four stories", 102),
            ([]))


# Faulty tests
class FaultyTestHotel(unittest.TestCase):
    """Class tests all faulty methods in the hotel class"""
    def test_hotel_creation(self):
        """Tests the faulty hotel creation method"""
        self.assertEqual(all_hotels.create_hotel("Four Seasons", 15), (
            "ID: Four Seasons and Hotel: 15"
            " can't be created"))

    def test_hotel_information(self):
        """Tests the faulty hotel information display method"""
        self.assertEqual(all_hotels.display_hotel_info("Four Seasons", 15), (
            "ID: Four Seasons and Hotel: 15 not found."))
