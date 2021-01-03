import unittest
from src.Adding_to_Book import AddingToBook
from src.Retrieving_from_Book import RetrievingFromBook
from src.Contact import Contact
import csv
import os


#aworks with TearDown but not with tearDown


class AddingToBookTest(unittest.TestCase):
    def tearDown(self):
        os.remove('Contact_Book.csv')
        with open('Updated_contact_Book.csv'):
            os.rename('Updated_contact_Book.csv', 'Contact_Book.csv')
    def test_create_new_contact(self):
        # first create contact object from input
        contact = Contact('Rajesh', '+65 12345678', '' ,'')
        AddingToBook.create_new_contact(contact)
        if contact.name == None:
            contact.name = ''
        if contact.phone == None:
            contact.phone = ''
        if contact.email == None:
            contact.email = ''
        if contact.address == None:
            contact.address = ''

        #here check if csv file has contact or not
        with open('Contact_Book.csv', 'r') as file:
            reader = csv.reader(file)
            self.assertIn([str(contact.name),str(contact.phone),str(contact.email),str(contact.address)], reader)
    def test_updating_contact(self):
        contact = Contact('Rajesh', '+65 12345678', '', '')
        if contact.name == None:
            contact.name = ''
        if contact.phone == None:
            contact.phone = ''
        if contact.email == None:
            contact.email = ''
        if contact.address == None:
            contact.address = ''
        AddingToBook.create_new_contact(contact)
        # we wil update the email of that contact and test it
        AddingToBook.update_existing_contact(['Name'], ['Rajesh'], ['Email ID'], ['Rajesh@outlook.com'])
        with open('Contact_Book.csv', 'r') as file:
            reader = csv.reader(file)
            self.assertIn(['Rajesh', '+65 12345678', 'Rajesh@outlook.com', ''], reader)
    def test_update_contact_when_3_records_exist(self):
        contact = Contact('Rajesh', '+65 12345678', None, None)
        AddingToBook.create_new_contact(contact)
        contact = Contact('Rajesh2', '+65 12345678', None, None)
        AddingToBook.create_new_contact(contact)
        contact = Contact('Rajesh3', '+65 12345678', None, None)
        AddingToBook.create_new_contact(contact)
        AddingToBook.update_existing_contact(['Name'], ['Rajesh2'], ['Email ID'], ['Rajesh@outlook.com'])
        with open('Contact_Book.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0:
                    if row[0] == 'Rajesh2':
                        self.assertEqual(row, ['Rajesh2', '+65 12345678', 'Rajesh@outlook.com', ''])
if __name__ == '__main__':
    unittest.main()
