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


# song artist set
song_library = [("Phantom Of The Opera", "Sarah Brightman"),
                ("Knocking On Heaven's Door", "Guns N' Roses"),
                ("Captain Nemo", "Sarah Brightman"),
                ("Patterns In The Ivy", "Opeth"),
                ("November Rain", "Guns N' Roses"),
                ("Beautiful", "Sarah Brightman"),
                ("Mal's Song", "Vixy and Tony")]


artists = set()
for song, artist in song_library:
    artists.add(artist)


# set operations
my_artists = {"Sarah Brightman", "Guns N' Roses",
              "Opeth", "Vixy and Tony"}
auburns_artists = {"Nickelback", "Guns N' Roses",
                   "Savage Garden"}


print("All: {}".format(my_artists.union(auburns_artists)))
print("Both: {}".format(auburns_artists.intersection(my_artists)))
print("Either but not both: {}".format(
    my_artists.symmetric_difference(auburns_artists)))


# set operations
bands = {"Guns N' Roses", "Opeth"}


print("my_artists is to bands:")
print("issuperset: {}".format(my_artists.issuperset(bands)))
print("issubset: {}".format(my_artists.issubset(bands)))
print("difference: {}".format(my_artists.difference(bands)))
print("*" * 20)
print("bands is to my_artists:")
print("issuperset: {}".format(bands.issuperset(my_artists)))
print("issubset: {}".format(bands.issubset(my_artists)))
print("difference: {}".format(bands.difference(my_artists)))


# oop pairs
"""
c = a + b
c = a.add(b)

l[0] = 5
l.setitem(0, 5) ?

d[key] = value
d.setitem(key, value)

for x in alist:
    #do something with x
it = alist.iterator()
while it.has_next():
    x = it.next()
    #do something with x
"""


# stupid adding integer
class SillyInt(int):
    def __add__(self, num):
        return 0
