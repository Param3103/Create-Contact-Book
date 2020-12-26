import copy
class RetrievingFromBook:

    def __init__(self, name, phone, address, email):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email

    def find_contact(self, contact_book, finder_keys, finder_values):
        contacts = []
        for contact in contact_book:
            found = True
            for finder_key in finder_keys:
                if (contact[finder_key] != finder_values[finder_keys.index(finder_key)]):
                    found = False
            if found is True:
                contacts.append(copy.deepcopy(contacr))
            else:
                continue
        return(contacts)

    def update_existing_contact(self, identifying_keys, identifying_values, tbc_keys, updated_values, contact_book):
        for contact in contact_book:
            found = True
            for identifying_key in identifying_keys:
                if (contact[identifying_key] != identifying_values[identifying_keys.index(identifying_key)]):
                    found = False
            if found is True:
                for tbc_key in tbc_keys:
                    contact_index = contact_book.index(contact)
                    contact[tbc_key] = updated_values[tbc_keys.index(tbc_key)]
                    contact_book[contact_index] = contact
            else:
                continue
        return(contact_book)
RetrievingFromBook