# string_creation
a = "hello"
b = 'world'
c = '''a multiple
line string'''
d = """More
multiple"""
e = ("Three " "Strings "
     "Together")


# format empty
template = "Hello {}, you are currently {}."
print(template.format('Dusty', 'writing'))


# format position
template2 = "Hello {0}, you are {1}. Your name is {0}."
print(template2.format('Dusty', 'writing'))


# format some positions broken
# template3 = "Hello {}, you are {}. Your name is {0}."
# print(template3.format('Dusty', 'writing'))  # crash
