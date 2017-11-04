# iterable - an object that has the __iter__ method defined
# iterator - an object that has both __iter__ and __next__ defined where __iter__ will return the iterator object and __next__ will return the next element in the iteration

'''
my_list = [1, 2, 3]  # iterable
list_ = iter(my_list)  # iterator
'''


class MyIterator:
    def __init__(self, letters):
        '''
        Constructor
        '''
        self.letters = letters
        self.position = 0

    def __iter__(self):
        '''
        Returns itself as an iterator
        '''
        return self

    def __next__(self):
        '''
        Returns the next letter in the sequence or
        raises StopIteration
        '''
        if self.position >= len(self.letters):
            raise StopIteration
        letter = self.letters[self.positon]
        self.position += 1
        return letter


if __name__ == '__main__':
    i = MyIterator('abcd')
    for item in i:
        print(item)
