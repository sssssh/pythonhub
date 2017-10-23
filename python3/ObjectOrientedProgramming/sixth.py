import string
import datetime
from collections import namedtuple, defaultdict, Counter
from functools import total_ordering


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


# counter frequency
def letter_frequency4(sentence):
    return Counter(sentence)


# counter poll
responses = [
    "vanilla",
    "chocolate",
    "vanilla",
    "vanilla",
    "caramel",
    "strawberry",
    "vanilla"
]


print(
    "The children voted for {} ice cream".format(
        Counter(responses).most_common(1)[0][0]
    )
)


d = defaultdict(tuple_counter)
# list tuple frequency
CHARACTERS = list(string.ascii_letters) + [" "]


def letter_frequency3(sentence):
    frequencies = [(c, 0) for c in CHARACTERS]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter, frequencies[index][1] + 1)
    return frequencies


# object comparison
@total_ordering
class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
        return "{}:{}".format(self.string, self.number)

    def __eq__(self, object):
        return all((
            self.string == object.string,
            self.number == object.number,
            self.sort_num == object.number
        ))
