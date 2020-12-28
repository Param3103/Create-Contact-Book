import csv
from Adding_to_Book import AddingToBook
from Retrieving_from_Book import RetrievingFromBook
# creating contact_book
"""
#this code adds data
with open('Contact_Book.csv', 'a') as file:
    fieldnames = ['Name', 'Phone No', 'Email ID', 'Address']
    writer = csv.writer(file)
    reader = csv.reader(file, delimiter=',')
    AddingToBook.creating_new_contact('Raj', '+65 92955893', None, None, writer)
"""
"""
#this code retrieves data
with open('Contact_Book.csv', 'r+') as file:
    writer = csv.writer(file)
    reader = csv.reader(file, delimiter=',')
    print(RetrievingFromBook.find_contact(reader, ['Name'], ['Raj']))
"""
with open('Contact_Book.csv', 'r+') as file:
    writer = csv.writer(file)
    reader = csv.reader(file, delimiter=',')
    reader = list(reader)
    print(reader)
    AddingToBook.update_existing_contact(['Name'], ['Raj'], ['Phone No'], ['+65 92955893'], reader, writer)
