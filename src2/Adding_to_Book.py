from Contact import Contact
class AddingToBook:
    def create_new_contact(contact, writer): #contact is Contact object
        writer.writerow([contact.name, contact.phone, contact.email, contact.address])
