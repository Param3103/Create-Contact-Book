import csv
from Adding_to_Book import AddingToBook
from Retrieving_from_Book import RetrievingFromBook
# creating contact_book

#this code adds data
"""
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
    for contact in RetrievingFromBook.find_contact(reader, ['Name'], ['Raj']):
        print(contact.name)

"""
with open('Contact_book.csv', 'r+') as file:
    writer = csv.writer(file)
    reader = csv.reader(file)
    AddingToBook.update_existing_contact(['Name'], ['Raj'], ['Email ID'], ['rituraj@gmail.com'], reader, writer)
