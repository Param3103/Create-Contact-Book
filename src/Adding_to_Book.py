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


    def update_existing_contact(identifying_keys, identifying_values, tbc_keys, new_values, contact_book):
        for key in identifying_keys:
            for contact in contact_book:
                if contact.key == identifying_values[identifying_keys.index(key)]:
                    for tbc_key in tbc_keys:
                        contact.tbc_key = new_values[tbc_keys.index(tbc_key)]
                        contact_book[contact_book.index(original_contact)] = contact
        return(contact_book)

AddingToBook