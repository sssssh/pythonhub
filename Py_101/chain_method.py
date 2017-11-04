from itertools import chain


my_list = ['foo', 'bar']
number = list(range(5))
cmd = ['ls', '/some/dir']
my_list.extend(cmd, number)
my_list = list(chain(['foo', 'bar'], cmd, number))


print(list(chain.from_iterable([cmd, number])))
