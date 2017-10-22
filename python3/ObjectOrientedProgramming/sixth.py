import datetime
from collections import namedtuple, defaultdict


# empty object
class MyObject:
    pass


# pass tuple to function
def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low) / 2), date)


mid_value, date = middle(("GOOG", 613.30, 625.86, 610.50),
                         datetime.date(2010, 1, 6))


# named tuple
Stock = namedtuple("Stock", "symbol current high low")
stock = Stock("FB", 75.00, high=75.03, low=74.90)


# dict stocks
stocks = {"GOOG": (613.30, 625.86, 610.50),
          "MSFT": (30.25, 30.70, 30.19)}


# random key dict
random_keys = {}
random_keys["astring"] = "somestring"
random_keys[5] = "aninteger"
random_keys[25.2] = "floats work too"
random_keys[("abc", 123)] = "so do tuples"


class AnObject:
    def __init__(self, avalue):
        self.avalue = avalue


my_object = AnObject(14)
random_keys[my_object] = "We can even store objects"
my_object.avalue = 12
try:
    random_keys[[1, 2, 3]] = "we can't store lists though"  # key (list) -> unhashable type: 'list'
except:
    print("unable to store list\n")

for key, value in random_keys.items():
    print("{} has value {}".format(key, value))


# setdefault frequency
def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequency[letter] = frequency + 1
    return frequency


# defaultdict frequency
def letter_frequency2(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


# defaultdict custom function
num_items = 0


def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])


d = defaultdict(tuple_counter)
