import csv
from Adding_to_Book import AddingToBook
from Retrieving_from_Book import RetrievingFromBook
# creating contact_book
with open('Contact_Book.csv', 'w') as file:
    fieldnames = ['Name', 'Phone No', 'Email ID', 'Address']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    reader = csv.DictReader(file)
    AddingToBook.update_existing_contact(['Name'], ['Param'], ['Email ID'], ['param.mehrotra@gmail.com'], reader)