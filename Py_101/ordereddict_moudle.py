from collections import OrderedDict


d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
new_d = OrderedDict(sorted(d.items()))


for key in reversed(new_d):
    print(key, new_d[key])
