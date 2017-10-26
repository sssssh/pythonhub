from collections import namedtuple


# iterator
class CapitalIterable:
    def __init__(self, _string):
        self._string = _string

    def __iter__(self):
        return CapitalIterator(self._string)


class CapitalIterator:
    def __init__(self, _string):
        self.words = [w.capitalize() for w in _string.split()]
        self._index = 0

    def __next__(self):
        if self._index == len(self.words):
            raise StopIteration()

        word = self.words[self._index]
        self._index += 1
        return word

    def __iter__(self):
        return self


# for loop converter
input_strings = ['1', '5', '28', '131', '3']
output_integers = []
for num in input_strings:
    output_integers.append(int(num))


# listcomp converter
listcomp_integers = [int(num) for num in input_strings]


# listcomp exclude
exclude_integers = [int(num) for num in input_strings if len(num) < 3]


# set comprehension
Book = namedtuple("Book", "author title genre")
books = [
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief Of Time", "fantasy"),
    Book("Le Guin", "The Dispossessed", "scifi"),
    Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
    Book("Turner", "The Thief", "fantasy"),
    Book("Phillips", "Preston Diamond", "western"),
    Book("Phillips", "Twice Upon A Time", "scifi"),
]
fantasy_authors = {
        b.author for b in books if b.genre == 'fantasy'}


# dict comprehension
fantasy_titles = {
    b.title: b for b in books if b.genre == 'fantasy'}


# log processor
existfilename = ''
newfilename = ''


with open(existfilename) as infile:
    with open(newfilename, "w") as outfile:
        warnings = (l for l in infile if "WARNING" in l)
        for l in warnings:
            outfile.write(l)
