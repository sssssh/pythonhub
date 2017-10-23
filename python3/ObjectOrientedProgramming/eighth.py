import datetime


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


# brace escape
template4 = """
public class {0} {{
    public static void main(String[] args) {{
        System.out.println("{1}");
    }}
}}"""

print(template4.format("MyClass", "print('hello world')"))


# format kw args
template5 = """
From: <{from_email}>
To: <{to_email}>
Subject: {subject}
{message}"""

print(template5.format(
    from_email="a@example.com",
    to_email="b@example.com",
    subject="You have mail!",
    message="Here's some mail for you. Hope you enjoy the message!"
))


# unlabelled kw
print("{} {label} {}".format("x", "y", label="z"))


# tuple dict format
emails = ("a@example.com", "b@example.com")
message = {
        'subject': "You Have Mail!",
        'message': "Here's some mail for you!"
        }

template6 = """
From: <{0[0]}>
To: <{0[1]}>
Subject: {message[subject]}
{message[message]}"""
print(template6.format(emails, message=message))


# tuple in dict format
message2 = {
        'emails': emails,
        'subject': "You Have Mail!",
        'message': "Here's some mail for you!"
        }
template7 = """
From: <{0[emails][0]}>
To: <{0[emails][1]}>
Subject: {0[subject]}
{0[message]}"""
print(template7.format(message2))


# object formatting
class EMail:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message


email2 = EMail("a@example.com", "b@example.com",
               "You Have Mail!",
               "Here's some mail for you!")

template = """
From: <{0.from_addr}>
To: <{0.to_addr}>
Subject: {0.subject}

{0.message}"""
print(template.format(email2))


# no format
subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax


print("Sub: ${0} Tax: ${1} Total: ${total}".format(
    subtotal, tax, total=total))


# currency format
print("Sub: ${0:0.2f} Tax: ${1:0.2f} "
      "Total: ${total:0.2f}".format(
          subtotal, tax, total=total))


# tabular
orders = [('burger', 2, 5),
          ('fries', 3.5, 1),
          ('cola', 1.75, 3)]


print("PRODUCT    QUANTITY    PRICE    SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print("{0:10s}{1: ^9d}    ${2: <8.2f}${3: >7.2f}".format(
        product, quantity, price, subtotal))


# format datetime
print("{0:%Y-%m-%d %I:%M%p }".format(
    datetime.datetime.now()))


# encode bytes
characters = b'\x63\x6c\x69\x63\x68\xe9'
print(characters)
print(characters.decode("latin-1"))


# decode unicode
characters = "cliché"
print(characters.encode("UTF-8"))
print(characters.encode("latin-1"))
print(characters.encode("CP437"))
print(characters.encode("ascii"))


# bytearray replace
b = bytearray(b"abcdefgh")
b[4:6] = b"\x15\xa3"
print(b)


# bytearray index
b = bytearray(b'abcdef')
b[3] = ord(b'g')
b[4] = 68
print(b)
