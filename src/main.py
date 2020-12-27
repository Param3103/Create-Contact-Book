import csv
from Adding_to_Book import AddingToBook
from Retrieving_from_Book import RetrievingFromBook
# creating contact_book
with open('Contact_Book.csv', 'r+') as file:
    fieldnames = ['Name', 'Phone No', 'Email ID', 'Address']
    writer = csv.writer(file)
    reader = csv.reader(file)
with open('Contact_Book.csv', 'a+') as file:
    writer = csv.writer(file)
    AddingToBook.creating_new_contact('Param', '94276963', None, None, writer)