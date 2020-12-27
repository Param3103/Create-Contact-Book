import csv


class RetrievingFromBook:
    def find_contact(contact_book, finder_keys, finder_values):
        contacts = []
        for row in contact_book:
            contact = dict(row)
            print(contact)
            found = True
            for finder_key in finder_keys:
                if contact[finder_key] != finder_values[finder_keys.index(finder_key)]:
                    found = False
            if found:
                contacts.append(contact)
            else:
                continue
        return (contacts)


RetrievingFromBook
