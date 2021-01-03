import unittest
from src.Adding_to_Book import AddingToBook
from src.Retrieving_from_Book import RetrievingFromBook
from src.Contact import Contact
import csv
import os
# not ok



class AddingToBookTest(unittest.TestCase):
    def setUp(self):
        self.contact = Contact('Rajesh', '+65 12345678', '', '')
    def tearDown(self):
        del self.contact
    def test_create_new_contact(self):
        # first create contact object from input
        AddingToBook.create_new_contact(self.contact)
        if self.contact.name == None:
            self.contact.name = ''
        if self.contact.phone == None:
            self.contact.phone = ''
        if self.contact.email == None:
            self.contact.email = ''
        if self.contact.address == None:
            self.contact.address = ''

        #here check if csv file has contact or not
        with open('Contact_Book.csv', 'r') as file:
            reader = csv.reader(file)
            self.assertIn([str(self.contact.name),str(self.contact.phone),str(self.contact.email),str(self.contact.address)], reader)
    def test_updating_contact(self):
        if self.contact.name == None:
            self.contact.name = ''
        if self.contact.phone == None:
            self.contact.phone = ''
        if self.contact.email == None:
            self.contact.email = ''
        if self.contact.address == None:
            self.contact.address = ''
        AddingToBook.create_new_contact(self.contact)
        # we wil update the email of that contact and test it
        AddingToBook.update_existing_contact(['Name'], ['Rajesh'], ['Email ID'], ['Rajesh@outlook.com'])
        with open('Contact_Book.csv', 'r') as file:
            reader = csv.reader(file)
            self.assertIn(['Rajesh', '+65 12345678', 'Rajesh@outlook.com', ''], reader)
    def test_update_contact_when_3_records_exist(self):
        self.contact = Contact('Rajesh', '+65 12345678', None, None)
        AddingToBook.create_new_contact(self.contact)
        self.contact = Contact('Rajesh2', '+65 12345678', None, None)
        AddingToBook.create_new_contact(self.contact)
        self.contact = Contact('Rajesh3', '+65 12345678', None, None)
        AddingToBook.create_new_contact(self.contact)
        AddingToBook.update_existing_contact(['Name'], ['Rajesh2'], ['Email ID'], ['Rajesh@outlook.com'])
        with open('Contact_Book.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0:
                    if row[0] == 'Rajesh2':
                        self.assertEqual(row, ['Rajesh2', '+65 12345678', 'Rajesh@outlook.com', ''])
if __name__ == '__main__':
    unittest.main()