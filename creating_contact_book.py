contact_book = []
class AddingToBook:

    def __init__(self, name, phone, address, email):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email

    def creating_new_contact(self):
        contact = {'name': self.name, 'phone': self.phone, 'address': self.address, 'email': self.email}
        contact_book.append(contact)

    def update_existing_contact(self, finder_keys, finder_values, tbc_keys, updated_values):
        for contact in contact_book:
            found = True
            for finder_key in finder_keys:
                if (contact[finder_key] != finder_values[finder_keys.index(finder_key)]):
                    found = False
            if found is True:
                for tbc_key in tbc_keys:
                    contact_index = contact_book.index(contact)
                    contact[tbc_key] = updated_values[tbc_keys.index(tbc_key)]
                    contact_book[contact_index] = contact
            else:
                continue