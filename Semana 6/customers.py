"""Module provides all the methods needed for the customer program."""
import json
from classes import Customer


class CustomerList(Customer):
    """Class used to create the different methods to modify Customers
        a needed"""
    def create_customer(self, customer_id, customer_name):
        try:
            get_name = str(customer_name)
            get_id = int(customer_id)

            self.file.append({'CUSTOMER_ID': get_id,
                              'CUSTOMER_NAME': get_name})

            with open(self.file_location, "w", encoding="utf-8") as outfile:
                json.dump(self.file, outfile, indent=1)

            return {'CUSTOMER_ID': get_id,
                    'CUSTOMER_NAME': get_name}
        except ValueError:

            return (f"ID: {customer_id} and cust: {customer_name}"
                    f" can't be created")

    def delete_customer(self, customer_id, customer_name):
        try:
            get_name = str(customer_name)
            get_id = int(customer_id)

            self.file.remove({'CUSTOMER_ID': get_id,
                              'CUSTOMER_NAME': get_name})

            with open(self.file_location, "w", encoding="utf-8") as outfile:
                json.dump(self.file, outfile, indent=1)

        except ValueError:
            print(f"ID: {customer_id} and cust: {customer_name}"
                  f" can't be deleted")

    def display_customer_info(self, customer_id, customer_name):
        match_found = False

        for info in self.file:
            get_name = str(info["CUSTOMER_NAME"])
            get_id = str(info["CUSTOMER_ID"])

            if str(customer_id) == get_id or customer_name == get_name:
                print(f"Customer found: {info["CUSTOMER_NAME"]}")
                print(f"With the ID: {info["CUSTOMER_ID"]}")
                match_found = True

                return (f"Customer found: {info["CUSTOMER_NAME"]}"
                        f"With the ID: {info["CUSTOMER_ID"]}")

        if match_found is not True:
            print(f"ID: {customer_id} and cust: {customer_name} not found.")
            return f"ID: {customer_id} and cust: {customer_name} not found."

    def modify_customer(self, customer_id, customer_name, new_id, new_name):
        match_found = False

        for info in self.file:
            get_name = str(info["CUSTOMER_NAME"])
            get_id = str(info["CUSTOMER_ID"])

            if str(customer_id) == get_id and customer_name == get_name:
                info["CUSTOMER_ID"] = new_id
                info["CUSTOMER_NAME"] = new_name
                match_found = True

        if match_found is not True:
            print(f"ID: {customer_id} and cust: {customer_name} not found.")
            return f"ID: {customer_id} and cust: {customer_name} not found."

        elif match_found:
            with open(self.file_location, "w", encoding="utf-8") as outfile:
                json.dump(self.file, outfile, indent=1)

            return {'CUSTOMER_ID': new_id,
                    'CUSTOMER_NAME': new_name}
