# ok
import unittest
from src.Adding_to_Book import AddingToBook
from src.Retrieving_from_Book import RetrievingFromBook
from src.Contact import Contact


class RetrievingFromBookTest(unittest.TestCase):
    def setUp(self):
        contact = Contact('Param', None, None, None)
        AddingToBook.create_new_contact(contact)

    def test_find_contact(self):
        contacts = RetrievingFromBook.find_contact(['Name'], ['Param'])
        for contact in contacts:
            self.assertEqual(contact, ['Param', '', '', ''])

if __name__ == '__main__':
    unittest.main()
