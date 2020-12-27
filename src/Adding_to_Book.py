import csv
class AddingToBook:

    def creating_new_contact(name, phone, email, address, contact_book):
        contact = [name, phone, address, email]
        contact_book.writerow(contact)
        return contact_book

# need to work on this
    def update_existing_contact(self, identifying_keys, identifying_values, tbc_keys, new_values, contact_book_reader, contact_book_writer):
        pass

AddingToBook