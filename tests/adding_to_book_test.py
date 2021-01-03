import unittest
from src.Adding_to_Book import AddingToBook
from src.Retrieving_from_Book import RetrievingFromBook
from src.Contact import Contact
import csv





class AddingToBookTest(unittest.TestCase):
    def test_create_new_contact(self):
        # first create contact object from input
        contact = Contact('Rajesh', '+65 12345678', None, None)
        with open('Contact_Book.csv', 'r+') as file:
            csv_writer = csv.writer(file)
            AddingToBook.create_new_contact(contact, csv_writer)
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
            for row in reader:
                if len(row) > 0:
                    self.assertEqual(row, [str(contact.name),str(contact.phone),str(contact.email),str(contact.address)])

    def test_updating_contact(self):
        pass
    def removing_contact(self):
        pass
    def test_update_contact_when_3_records_exist(self):
        pass
        """
        contact = Contact('Rajesh', '+65 12345678', None, None)
        AddingToBook.creating_new_contact(contact)
        contact = Contact('Rajesh2', '+65 12345678', None, None)
        AddingToBook.creating_new_contact(contact)
        contact = Contact('Rajesh3', '+65 12345678', None, None)
        AddingToBook.creating_new_contact(contact)
        """

if __name__ == '__main__':
    unittest.main()
