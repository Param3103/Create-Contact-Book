import csv


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
        return (contacts)


RetrievingFromBook
