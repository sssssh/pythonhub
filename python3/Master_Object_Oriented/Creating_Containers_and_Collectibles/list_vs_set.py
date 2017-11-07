import timeit
timeit.timeit('l.remove(10); l.append(10)', 'l = list(range(20))')
timeit.timeit('l.remove(10); l.add(10)', 'l = set(range(20))')
