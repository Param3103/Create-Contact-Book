class AddingToBook:

    def __init__(self, name, phone, address, email):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email

    def creating_new_contact(self, contact_book):
        contact = {'Name': self.name, 'Phone No': self.phone, 'Address': self.address, 'Email ID': self.email}
        contact_book.writerow(contact)
        return(contact_book)

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
AddingToBook