# any
print(any([0, 0, 1, 0]))
widget_one = ''
widget_two = ''
widget_three = 'button'
widgets_exist = any([widget_one, widget_two, widget_three])
print(widgets_exist)


# enumerate
my_string = 'abcdefg'
for pos, letter in enumerate(my_string):
    print(pos, letter)


# eval
var = 10
source = 'var * 2'
print(eval(source))


# filter
def less_than_ten(x):
    return x < 10


my_list = [1, 2, 3, 10, 11, 12]
for item in filter(less_than_ten, my_list):
    print(item)


# map
def doubler(x):
    return x * 2


my_list = [1, 2, 3, 4, 5]
for item in map(doubler, my_list):
    print(item)
