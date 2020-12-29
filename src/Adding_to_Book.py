from Contact import Contact
import re

class AddingToBook:
    def creating_new_contact(name, phone, email, address, writer):
        contact = Contact(name, phone, email, address)
        writer.writerow([contact.name, contact.phone, contact.email, contact.address])

# need to work on this
    def update_existing_contact(finder_keys, finder_values, tbc_keys, new_values, contact_book_reader, contact_book_writer):
        fieldnames = ['Name', 'Phone No', 'Email ID', 'Address']
        contacts = []
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
                    contacts.append(contact)
                else:
                    continue
        for old_contact in contacts:
            contact = Contact
            contact.name = old_contact[0]
            contact.phone = old_contact[1]
            contact.address = old_contact[3]
            contact.email = old_contact[2]
            contacts[contacts.index(old_contact)] = contact

       # contacts has all that need to be updated
        for contact in contacts:
            print([contact.name, contact.phone, contact.email, contact.address])
            old_contact = contact
            for tbc_key in tbc_keys:
                if tbc_key == 'Name':
                    contact.name = new_values[tbc_keys.index(tbc_key)]
                elif tbc_key == 'Phone No':
                    contact.phone = new_values[tbc_keys.index(tbc_key)]
                elif tbc_key == 'Email ID':
                    contact.email = new_values[tbc_keys.index(tbc_key)]
                elif tbc_key == 'Address':
                    contact.address = new_values[tbc_keys.index(tbc_key)]
            contact_book_writer.writerow(contact)
AddingToBook
"""
find contact
fieldnames = ['Name', 'Phone No', 'Email ID', 'Address']
        contacts = []
        for contact in contact_book:
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
                    contacts.append(contact)
                else:
                    continue
        for old_contact in contacts:
            contact = Contact
            contact.name = old_contact[0]
            contact.phone = old_contact[1]
            contact.address = old_contact[3]
            contact.email = old_contact[2]
            contacts[contacts.index(old_contact)] = contact
        return (contacts)
"""