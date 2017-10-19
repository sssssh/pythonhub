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








