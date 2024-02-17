"""Module providing all classes used in the proyect."""
from abc import ABC, abstractmethod
import json


class Hotel(ABC):
    """Hotel class blueprint"""
    def __init__(self):
        # We open both of our files as Json format
        self.file_location = "resources/Hotel.List.json"

        with open(self.file_location, "r", encoding="utf-8") as data_file1:
            self.file = json.load(data_file1)

    @abstractmethod
    def create_hotel(self, hotel_id, hotel_name):
        """Hotel creation method, adds hotel in Json"""

    @abstractmethod
    def delete_hotel(self, hotel_id, hotel_name):
        """Hotel deletion method, removes hotel in Json"""

    @abstractmethod
    def display_hotel_info(self, hotel_id, hotel_name):
        """Hotel display method, finds a hotel in Json"""

    @abstractmethod
    def create_room_reservation(self, hotel_id, hotel_name, room):
        """Hotel reservation creation method, adds hotel number in Json"""

    @abstractmethod
    def cancel_room_reservation(self, hotel_id, hotel_name, room):
        """Hotel reservation deletion method, removes hotel number in Json"""


class Customer(ABC):
    """Customer class blueprint"""
    def __init__(self):
        # We open both of our files as Json format
        self.file_location = "resources/Customer.List.json"
        with open(self.file_location, "r", encoding="utf-8") as data_file1:
            self.file = json.load(data_file1)

    @abstractmethod
    def create_customer(self, customer_id, customer_name):
        """Customer creation method, adds customer in Json"""

    @abstractmethod
    def delete_customer(self, customer_id, customer_name):
        """Customer deletion method, adds customer in Json"""

    @abstractmethod
    def display_customer_info(self, customer_id, customer_name):
        """Customer display method, finds a customer in Json"""

    @abstractmethod
    def modify_customer(self, customer_id, customer_name, new_id, new_name):
        """Customer modification method, modifies an existen customer
           in the Json file"""


class Reservation(ABC):
    """Reservation class blueprint"""
    def __init__(self):
        # We open both of our files as Json format
        self.file_location = "resources/Reservation.List.json"

        with open(self.file_location, "r", encoding="utf-8") as data_file1:
            self.file = json.load(data_file1)

    @abstractmethod
    def create_a_reservation(self, c_id, h_id, room, f_date, t_date):
        """Reservation creation method, adds a reservation in Json"""

    @abstractmethod
    def cancel_a_reservation(self, c_id, h_id, room, f_date, t_date):
        """Reservation deletion method, deletes a reservation in Json"""
