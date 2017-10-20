# inheriting from object
class SubClass(object):
    pass


# simple contact class to inherit from
class Contact:
    all_contacts = []  # global variable

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)  # the way call the all_contacts


# contact inherit supplier
class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send"
              "{} order to {}".format(order, self.name))


# contact list inheritance
class ContactList(list):  # inheriting from list
    def search(self, name):  # add new method search contact by name
        """Return all contacts that contain the search value
        in their name."""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact1:
    all_contacts = ContactList()  # instance

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


# long name dictionary
class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest


# friend -> overrides init
class Friend(Contact):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
