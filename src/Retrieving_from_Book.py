import copy
class RetrievingFromBook:
    def find_contact(contact_book, finder_keys, finder_values):
        contacts = []
        for contact in contact_book:
            found = True
            for finder_key in finder_keys:
                if (contact[finder_key] != finder_values[finder_keys.index(finder_key)]):
                    found = False
            if found is True:
                contacts.append(copy.deepcopy(contact))
            else:
                continue
        return(contacts)
RetrievingFromBook 
