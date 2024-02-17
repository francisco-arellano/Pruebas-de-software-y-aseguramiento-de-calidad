"""Module provides all the methods needed for the hotel program."""
import json
from classes import Hotel


class HotelList(Hotel):
    """Class used to create the different methods to modify Hotels as needed"""
    def create_hotel(self, hotel_id, hotel_name):
        try:
            get_name = str(hotel_name)
            get_id = int(hotel_id)

            self.file.append({'HOTEL_ID': get_id,
                              'HOTEL_NAME': get_name,
                              'RESERVED_ROOMS': []})

            with open(self.file_location, "w", encoding="utf-8") as outfile:
                json.dump(self.file, outfile, indent=1)

            return {'HOTEL_ID': get_id,
                    'HOTEL_NAME': get_name,
                    'RESERVED_ROOMS': []}

        except ValueError:

            return (f"ID: {hotel_id} and Hotel: {hotel_name}"
                    f" can't be created")

    def delete_hotel(self, hotel_id, hotel_name):
        try:
            get_name = str(hotel_name)
            get_id = int(hotel_id)

            self.file.remove({'HOTEL_ID': get_id,
                              'HOTEL_NAME': get_name,
                              'RESERVED_ROOMS': []})
            with open(self.file_location, "w", encoding="utf-8") as outfile:
                json.dump(self.file, outfile, indent=1)

        except ValueError:
            print(f"ID: {hotel_id} and hotel: {hotel_name}"
                  f" can't be deleted")

    def display_hotel_info(self, hotel_id, hotel_name):
        match_found = False

        for info in self.file:
            get_name = str(info["HOTEL_NAME"])
            get_id = str(info["HOTEL_ID"])

            if str(hotel_id) == get_id or hotel_name == get_name:

                match_found = True

                return (f"Hotel found: {info["HOTEL_NAME"]}"
                        f" With the ID: {info["HOTEL_ID"]}"
                        f" Reserved rooms: {info["RESERVED_ROOMS"]}")

        if match_found is not True:
            print(f"ID: {hotel_id} and Hotel: {hotel_name} not found.")
            return f"ID: {hotel_id} and Hotel: {hotel_name} not found."

    def create_room_reservation(self, hotel_id, hotel_name, room):
        match_found = False

        for info in self.file:
            get_name = str(info["HOTEL_NAME"])
            get_id = str(info["HOTEL_ID"])

            if str(hotel_id) in get_id and hotel_name in get_name:
                get_rooms = info["RESERVED_ROOMS"]
                get_rooms.append(room)

                info["RESERVED_ROOMS"] = get_rooms
                match_found = True

                with open(self.file_location, "w", encoding="utf-8") as file:
                    json.dump(self.file, file, indent=1)

                return info["RESERVED_ROOMS"]

        if match_found is not True:
            print(f"ID: {hotel_id} and Hotel: {hotel_name} not found.")
            return print(f"ID: {hotel_id} and Hotel: {hotel_name} not found.")

    def cancel_room_reservation(self, hotel_id, hotel_name, room):
        match_found = False

        for info in self.file:
            get_name = str(info["HOTEL_NAME"])
            get_id = str(info["HOTEL_ID"])

            if str(hotel_id) in get_id and hotel_name in get_name:
                get_rooms = info["RESERVED_ROOMS"]
                get_rooms.remove(room)

                info["RESERVED_ROOMS"] = get_rooms
                match_found = True

                with open(self.file_location, "w", encoding="utf-8") as file:
                    json.dump(self.file, file, indent=1)

                return info["RESERVED_ROOMS"]

        if match_found is not True:
            print(f"ID: {hotel_id} and Hotel: {hotel_name} not found.")
            return print(f"ID: {hotel_id} and Hotel: {hotel_name} not found.")
