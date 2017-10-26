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
