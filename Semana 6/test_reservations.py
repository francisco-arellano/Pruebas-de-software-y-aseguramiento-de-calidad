"""Module provides a way to test the methods used in ReservationList class."""
import unittest
from reservations import ReservationList

all_reservations = ReservationList()


# Working tests
class TestReservation(unittest.TestCase):
    """Class tests all working methods in the reservation class"""
    def test_reservation_creation(self):
        """Tests the reservation creation method"""
        self.assertEqual(
            all_reservations.create_a_reservation(9876,
                                                  12,
                                                  123,
                                                  "01/14/23",
                                                  "01/15/23"), {
                                                  'HOTEL_ID': '12',
                                                  'CUSTOMER_ID': '9876',
                                                  'ROOM': 123,
                                                  'FROM_DATE': '01/14/23',
                                                  'TO_DATE': '01/15/23'})

    def test_reservation_deletion(self):
        """Tests the reservation deletion method"""
        self.assertNotIn(
            all_reservations.cancel_a_reservation(9876,
                                                  12,
                                                  123,
                                                  "01/14/23",
                                                  "01/15/23"), {
                                                  'HOTEL_ID': '12',
                                                  'CUSTOMER_ID': '9876',
                                                  'ROOM': 123,
                                                  'FROM_DATE': '01/14/23',
                                                  'TO_DATE': '01/15/23'})


# Faulty tests
class FaultyTestReservation(unittest.TestCase):
    """Class tests all faulty methods in the reservation class"""
    def test_reservation_creation(self):
        """Tests the faulty reservation creation method"""
        self.assertEqual(
            all_reservations.create_a_reservation(1234,
                                                  "a",
                                                  123,
                                                  "01/14/23",
                                                  "01/15/23"), (
                                                  "ID: 1234 "
                                                  "and cust: a not found."))

    def test_reservation_deletion(self):
        """Tests the faulty reservation deletion method"""
        self.assertEqual(
            all_reservations.cancel_a_reservation(1234,
                                                  2,
                                                  123,
                                                  "01/14/23",
                                                  "01/15/23"), (
                                                  "ID: 1234 "
                                                  "and cust: 2 not found."))
        self.assertEqual(
            all_reservations.cancel_a_reservation(9876,
                                                  12,
                                                  102,
                                                  "01/14/22",
                                                  "01/15/23"), (
                                                      "Room, forward date"
                                                      " and to date "
                                                      "are invalid."))
