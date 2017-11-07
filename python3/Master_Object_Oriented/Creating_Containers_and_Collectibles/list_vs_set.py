import timeit
timeit.timeit('l.remove(10); l.append(10)', 'l = list(range(20))')
timeit.timeit('l.remove(10); l.add(10)', 'l = set(range(20))')

# using two parallet lists vs. a mapping
timeit.timeit('i= k.index(10); v[i]= 0', 'k=list(range(20)); v=list(range(20))')
timeit.timeit('m[10]= 0', 'm=dict(zip(list(range(20)),list(range(20))))')
