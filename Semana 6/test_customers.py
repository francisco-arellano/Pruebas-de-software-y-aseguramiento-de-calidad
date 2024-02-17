"""Module provides a way to test the methods used in CustomerList class."""
import unittest
from customers import CustomerList

all_customers = CustomerList()


# Working tests
class TestCustomer(unittest.TestCase):
    """Class tests all working methods in the customer class"""
    def test_customer_creation(self):
        """Tests the customer creation method"""
        self.assertEqual(all_customers.create_customer(5678, "Pepe"), {
                        'CUSTOMER_ID': 5678,
                        'CUSTOMER_NAME': 'Pepe'})
        self.assertEqual(all_customers.create_customer(1111, "Carlos"), {
                        'CUSTOMER_ID': 1111,
                        'CUSTOMER_NAME': 'Carlos'})

    def test_customer_deletion(self):
        """Tests the customer deletion method"""
        self.assertNotIn(all_customers.delete_customer(1111, "Carlos"), {
                        'CUSTOMER_ID': 1111,
                        'CUSTOMER_NAME': 'Carlos'})

    def test_customer_info(self):
        """Tests the customer information display method"""
        self.assertEqual(all_customers.display_customer_info(1111, "Carlos"), (
            "ID: 1111 and cust: Carlos not found."))

    def test_modify_customer(self):
        """Tests the customer information modification method"""
        self.assertEqual(all_customers.modify_customer(
                        5678, "Pepe", 5678, "Juan"), {
                        'CUSTOMER_ID': 5678,
                        'CUSTOMER_NAME': 'Juan'})


# Faulty tests
class FaultyTestCustomer(unittest.TestCase):
    """Class tests all faulty methods in the customer class"""
    def test_customer_creation(self):
        """Tests the faulty customer creation method"""
        self.assertEqual(all_customers.create_customer("Jorge", 1234), (
            "ID: Jorge and cust: 1234"
            " can't be created"))

    def test_customer_info(self):
        """Tests the faulty customer information display method"""
        self.assertEqual(all_customers.display_customer_info(1234, "Jorge"), (
            "ID: 1234 and cust: Jorge not found."))
