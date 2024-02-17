"""Module provides all the methods needed for the reservation program."""
import json
from classes import Reservation
from customers import CustomerList
from hotels import HotelList

all_customers = CustomerList()
all_hotels = HotelList()


class ReservationList(Reservation):
    """Class used to create the different methods to modify
       reservations as needed"""
    def create_a_reservation(self, c_id, h_id, room, f_date, t_date):
        match_found = False

        for c_info in all_customers.file:
            for h_info in all_hotels.file:
                get_cus_id = str(c_info["CUSTOMER_ID"])
                get_hot_id = str(h_info["HOTEL_ID"])

                try:
                    if get_cus_id == str(c_id) and get_hot_id == str(h_id):

                        match_found = True
                        self.file.append({
                            'HOTEL_ID': get_hot_id,
                            'CUSTOMER_ID': get_cus_id,
                            'ROOM': room,
                            'FROM_DATE': f_date,
                            'TO_DATE': t_date
                            })

                        with open(self.file_location,
                                  "w", encoding="utf-8") as f:
                            json.dump(self.file, f, indent=1)

                        return {
                            'HOTEL_ID': get_hot_id,
                            'CUSTOMER_ID': get_cus_id,
                            'ROOM': room,
                            'FROM_DATE': f_date,
                            'TO_DATE': t_date
                            }

                except ValueError:
                    print("Room, forward date and to date are invalid.")
                    return "Room, forward date and to date are invalid."

        if match_found is not True:
            print(f"ID: {c_id} and cust: {h_id} not found.")
            return f"ID: {c_id} and cust: {h_id} not found."

    def cancel_a_reservation(self, c_id, h_id, room, f_date, t_date):
        match_found = False

        for c_info in all_customers.file:
            for h_info in all_hotels.file:
                get_cus_id = str(c_info["CUSTOMER_ID"])
                get_hot_id = str(h_info["HOTEL_ID"])

                try:
                    if get_cus_id == str(c_id) and get_hot_id == str(h_id):

                        match_found = True
                        self.file.remove({
                            'HOTEL_ID': get_hot_id,
                            'CUSTOMER_ID': get_cus_id,
                            'ROOM': room,
                            'FROM_DATE': f_date,
                            'TO_DATE': t_date
                            })

                        with open(self.file_location,
                                  "w", encoding="utf-8") as f:
                            json.dump(self.file, f, indent=1)

                        print({
                            'HOTEL_ID': get_hot_id,
                            'CUSTOMER_ID': get_cus_id,
                            'ROOM': room,
                            'FROM_DATE': f_date,
                            'TO_DATE': t_date
                            })

                except ValueError:
                    print("Room, forward date and to date are invalid.")
                    return "Room, forward date and to date are invalid."

        if match_found is not True:
            print(f"ID: {c_id} and cust: {h_id} not found.")
            return f"ID: {c_id} and cust: {h_id} not found."
