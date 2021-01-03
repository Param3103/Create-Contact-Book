import csv
from src.Contact import Contact

class RetrievingFromBook:
    def find_contact(finder_keys, finder_values):
        with open('Contact_Book.csv', 'r') as contact_book:
            fieldnames = ['Name', 'Phone No', 'Email ID', 'Address']
            contacts = []
            for contact in contact_book:
                if len(contact) == 0:
                    pass
                else:
                    temp_contact = []
                    word = ''
                    for i in contact:
                        if i != ',':
                            word += i
                        else:
                            temp_contact.append(word)
                            word = ''
                    temp_contact.append(word)
                    contact = temp_contact
                    temp = contact
                    found = True
                    for finder_key in finder_keys:
                        if contact[fieldnames.index(finder_key)] != finder_values[finder_keys.index(finder_key)]:
                            found = False
                            contact = temp
                        else:
                            contact = temp
                    if found:
                        contact[3] = contact[3][0:-2]
                        contacts.append(contact)
                    else:
                        continue
        return (contacts)


RetrievingFromBook