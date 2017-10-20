import random


# even integers
class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)


# exception quits
def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"


# method calls excepting
def call_exceptor():
    print("call_exceptor starts here...")
    no_return()
    print("an exception was raised...")
    print("...so these lines don't run")


# try except
try:
    no_return
except:
    print("I caught an exception")
print("executed after the exception")


# catch specific exception
def funny_division(anumber):
    try:
        return 100 / anumber
    except ZeroDivisionError:
        return "Silly wabbit, you can't divide by zero!"


print(funny_division(0))
print(funny_division(50.0))
print(funny_division("hello"))


# catch multiple exceptions
def funny_division2(anumber):
    try:
        if anumber == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / anumber
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"


for val in (0, "hello", 50.0, 13):
    print("Testing {}:".format(val), end=" ")
    print(funny_division2(val))


# catch multiple different
def funny_division3(anumber):
    try:
        if anumber == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / anumber
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        raise


for val in (0, "hello", 50.0, 13):
    print("Testing %s:" % val, end=" ")
    print(funny_division3(val))


# catch as keyword
try:
    raise ValueError("This is an argument")
except ValueError as e:
    print("The exception arguments were", e.args)


# finally and else
some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("An error")
except ValueError:
    print("Caught a ValueError")
except TypeError:
    print("Caught a TypeError")
except Exception as e:
    print("Caught some other error: %s" % e.__class__.__name__)
else:
    print("This code called if there is no exception")
finally:
    print("This cleanup code is always called")


# defining an exception
class InvalidWithdrawal(Exception):
    pass


raise InvalidWithdrawal("You don't have $50 in your account")


# exception with custom args
class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__("account doesn't have ${}".format(
            amount))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance


raise InvalidWithdrawal(25, 50)


# handle custom exception
try:
    raise InvalidWithdrawal(25, 50)
except InvalidWithdrawal as e:
    print("I'm sorry, but your withdrawal is "
          "more than your balance by "
          "${}".format(e.overage()))


# branching vs exceptions
def divide_with_exception(number, divisor):
    try:
        print("{} / {} = {}".format(
            number, divisor, number / divisor * 1.0))
    except ZeroDivisionError:
        print("You can't divide by zero")


def divide_with_if(number, divisor):
    if divisor == 0:
        print("You can't divide by zero")
    else:
        print("{} / {} = {}".format(
            number, divisor, number / divisor * 1.0))


divide_with_exception(10, 5)
divide_with_if(10, 5)
divide_with_if(10, 0)
divide_with_exception(10, 0)


# inventory mock object
class Inventory:
    def lock(self, item_type):
        '''Select the type of item that is going to
        be manipulated. This method will lock the
        item so nobody else can manipulate the
        inventory until it's returned. This prevents
        selling the same item to two different
        customers.'''
        pass

    def unlock(self, item_type):
        '''Release the given type so that other
        customers can access it.'''
        pass

    def purchase(self, item_type):
        '''If the item is not locked, raise an
        exception. If the itemtype does not exist,
        raise an exception. If the item is currently
        out of stock, raise an exception. If the item
        is available, subtract one item and return
        the number of items left.'''
        pass
