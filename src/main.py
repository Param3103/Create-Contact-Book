import csv
from Adding_to_Book import AddingToBook
from Retrieving_from_Book import RetrievingFromBook
# creating contact_book
with open('Contact_Book.csv', 'r+') as file:
    fieldnames = ['Name', 'Phone No', 'Email ID', 'Address']
    writer = csv.writer(file)
    reader = csv.reader(file)
    AddingToBook.creating_new_contact('Param', '+65 94276963', None, None, writer)
with open('Contact_Book.csv', 'a+') as file:
    writer = csv.writer(file)
    reader = csv.reader(file)
    print(RetrievingFromBook.find_contact(reader, ['Name'], ['Param']))