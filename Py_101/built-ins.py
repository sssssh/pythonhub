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
