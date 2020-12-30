import unittest
from Contact import Contact

class AddingToBookTest(unittest.TestCase):
    def test_creating_new_contact(self):
        # first create contact object from input
        contact = Contact('Rajesh', '+65 12345678', None, None)
        AddingToBook.creating_new_contact(contact)
        print('test')
        #here check if csv file has contact or not
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


if __name__ == '__main__':
    unittest.main()
