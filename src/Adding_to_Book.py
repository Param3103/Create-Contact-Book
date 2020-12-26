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

# need to work on this
    def update_existing_contact(self, identifying_keys, identifying_values, tbc_keys, new_values, contact_book_reader):
        for key in identifying_keys:
            for contacts in contact_book_reader:
                for contact in contacts: #something is wrong here
                    if contact.key == identifying_values[identifying_keys.index(key)]:
                        for tbc_key in tbc_keys:
                            original_contact = contact
                            contact.tbc_key = new_values[tbc_keys.index(tbc_key)]
                            self[contact_book_reader.index(original_contact)] = contact
        return(self)

AddingToBook