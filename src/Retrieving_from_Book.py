import csv
from src.Contact import Contact

class RetrievingFromBook:
    def find_contact(contact_book, finder_keys, finder_values):
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


RetrievingFromBook