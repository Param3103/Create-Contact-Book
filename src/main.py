import csv
from Adding_to_Book import AddingToBook
from Retrieving_from_Book import RetrievingFromBook
import os
# creating contact_book


"""
#this code adds data

with open('Contact_Book.csv', 'a') as file:
    writer = csv.writer(file)
    AddingToBook.creating_new_contact('Raj', '+65 92955893', None, None, writer)
"""

"""
#this code retrieves data

with open('Contact_Book.csv', 'r+') as file:
    reader = csv.reader(file, delimiter=',')
    for contact in RetrievingFromBook.find_contact(reader, ['Name'], ['Raj']):
        print(contact.name)

"""
"""
#this code updates data into same file

with open('Contact_book.csv', 'r+') as reader_file:
    with open('Updated_Contact_Book.csv', 'w+') as writer_file:
        writer = csv.writer(writer_file)
        reader = csv.reader(reader_file)
        AddingToBook.update_existing_contact(['Name'], ['Raj'], ['Email ID'], ['rituraj@gmail.com'], reader, writer)
os.remove('Contact_Book.csv')
os.rename('Updated_Contact_book.csv', 'Contact_Book.csv')
"""
