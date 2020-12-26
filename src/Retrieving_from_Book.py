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
RetrievingFromBook