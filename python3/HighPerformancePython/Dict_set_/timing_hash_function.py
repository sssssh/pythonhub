import string
import timeit


class BadHash(str):
    def __hash__(self):
        return 42


class GoodHash(str):
    def __hash__(self):
        '''
        This is a slightly optimized version of twoletter_hash
        '''
        return ord(self[1]) + 26 * ord(self[0]) - 2619


baddict = set()
gooddict = set()


for i in string.ascii_lowercase:
    for j in string.ascii_letters:
        key_ = i + j
        baddict.add(BadHash(key_))
        gooddict.add(GoodHash(key_))

print(baddict)
print(gooddict)


badtime = timeit.repeat(
    "key in baddict",
    setup="from __main__ import baddict, BadHash; key = BadHash('zz')",
    repeat=3,
    number=1000000,
)


goodtime = timeit.repeat(
    "key in gooddict",
    setup="from __main__ import gooddict, GoodHash; key = GoodHash('zz')",
    repeat=3,
    number=1000000,
)


print("Min lookup time for baddict: ", min(badtime))
print("Min lookup time for gooddict: ", min(goodtime))