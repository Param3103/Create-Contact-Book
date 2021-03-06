from src.Contact import Contact
import csv
import os

class AddingToBook:
    def create_new_contact(contact):  # contact is Contact object
        with open('Contact_Book.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([contact.name, contact.phone, contact.email, contact.address])

    def update_existing_contact(finder_keys, finder_values, tbc_keys, new_values):
        with open('Contact_book.csv', 'r') as reader:
            with open('Updated_Contact_Book.csv', 'w+') as writer:
                contact_book_reader = csv.reader(reader)
                contact_book_writer = csv.writer(writer)
                fieldnames = ['Name', 'Phone No', 'Email ID', 'Address']
                tbu_contacts = []
                updated_contacts = []
                for contact in contact_book_reader:
                    if len(contact) == 0:
                        pass
                    else:
                        temp = contact
                        found = True
                        for finder_key in finder_keys:
                            if contact[fieldnames.index(finder_key)] != finder_values[finder_keys.index(finder_key)]:
                                found = False
                                contact = temp
                            else:
                                contact = temp
                        if found:
                            tbu_contacts.append(contact)
                        else:
                            contact_book_writer.writerow(contact)
                for old_contact in tbu_contacts:
                    contact = Contact
                    contact.name = old_contact[0]
                    contact.phone = old_contact[1]
                    contact.address = old_contact[3]
                    contact.email = old_contact[2]
                    tbu_contacts[tbu_contacts.index(old_contact)] = contact

                # contacts has all that needs to be updated
                for contact in tbu_contacts:
                    for tbc_key in tbc_keys:
                        if tbc_key == 'Name':
                            contact.name = new_values[tbc_keys.index(tbc_key)]
                        elif tbc_key == 'Phone No':
                            contact.phone = new_values[tbc_keys.index(tbc_key)]
                        elif tbc_key == 'Email ID':
                            contact.email = new_values[tbc_keys.index(tbc_key)]
                        elif tbc_key == 'Address':
                            contact.address = new_values[tbc_keys.index(tbc_key)]
                    new_contact = [contact.name, contact.phone, contact.email, contact.address]
                    contact_book_writer.writerow(new_contact)

        os.remove('Contact_Book.csv')
        os.rename('Updated_Contact_book.csv', 'Contact_Book.csv')
AddingToBook