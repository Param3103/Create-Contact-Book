import unittest
from src.Adding_to_Book import AddingToBook
from src.Retrieving_from_Book import RetrievingFromBook
# from src.Contact import Contact for ssome reason this is not working
import csv

class Contact:
    def __init__(self, name, phone, address, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

with open('Contact_Book.csv', 'r+') as file:
    csv_reader = csv.reader(file)
    csv_writer = csv.writer(file)


class AddingToBookTest(unittest.TestCase):
    def test_creating_new_contact(self):
        # first create contact object from input
        contact = Contact('Rajesh', '+65 12345678', None, None)
        AddingToBook.creating_new_contact(contact, csv_writer)

        #here check if csv file has contact or not
        self.assertIn(contact, 'Contact_Book.csv')
    """
    def test_updating_contact(self):
        pass
    def removing_contact(self):
        pass
    def test_something(self):
        self.assertEqual(True, False)
    def test_update_contact_when_3_records_exist(self):
        contact = Contact('Rajesh', '+65 12345678', None, None)
        AddingToBook.creating_new_contact(contact)
        contact = Contact('Rajesh2', '+65 12345678', None, None)
        AddingToBook.creating_new_contact(contact)
        contact = Contact('Rajesh3', '+65 12345678', None, None)
        AddingToBook.creating_new_contact(contact)
"""

if __name__ == '__main__':
    unittest.main()
