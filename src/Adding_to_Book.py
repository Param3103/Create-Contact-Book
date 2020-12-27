import csv
class AddingToBook:

    def creating_new_contact(name, phone, email, address, contact_book):
        contact = {'Name' : name, 'Phone No' : phone, 'Address' : address, 'Email ID' : email}
        contact_book.writerow(contact)
        return(contact_book)

# need to work on this 
    def update_existing_contact(self, identifying_keys, identifying_values, tbc_keys, new_values, contact_book_reader):
        pass


AddingToBook
