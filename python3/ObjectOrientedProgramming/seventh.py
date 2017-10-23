from operator import itemgetter


# reversible objects
normal_list = [1, 2, 3, 4, 5]


class CustomSequence():
    def __len__(self):
        return 5

    def __getitem__(self, index):
        return "x{0}".format(index)


class FunkyBackwards():
    def __reversed__(self):
        return "BACKWARDS!"


for seq in normal_list, CustomSequence(), FunkyBackwards():
    print('----', seq)
    print("\n{}: ".format(seq.__class__.__name__), end="")
    for item in reversed(seq):
        print(item, end=", ")


# enumerate line numbers
def enumerate_line(filename):
    with open(filename) as files:
        for index, line in enumerate(files):
            print("{0}: {1}".format(index+1, line), end='')


# zip to enumerate
def zip_enumerate(container):
    return zip(range(len(container)), container)


# enumerate max min
def min_max_indexes(seq):
    minimum = min(enumerate(seq), key=itemgetter(1))
    maximum = max(enumerate(seq), key=itemgetter(1))
    return minimum[0], maximum[0]
