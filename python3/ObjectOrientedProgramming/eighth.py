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
