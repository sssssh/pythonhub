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


# friend -> overrides init super
class Friend1(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


# send mail
class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)
        # Add e-mail logic here


class EmailableContact(Contact, MailSender):
    # Add logic here
    pass


# holder friend address
class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code


# multi friend
class Friend2(Contact, AddressHolder):
    def __init__(self, name, email, phone,
                 street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(
            self, street, city, state, code)
        self.phone = phone


_a_friend = ['a', 'a@1', 123, 'Baker', 'UK', 'Unknown', 123456]
_friend = Friend2(*_a_friend)


# contrived diamond
class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Left Subclass")
        self.num_left_calls += 1


class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Right Subclass")
        self.num_right_calls += 1


class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self):
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print("Calling method on Subclass")
        self.num_sub_calls += 1
