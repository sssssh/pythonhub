def doubler_generator():
    number = 2
    while True:
        yield number
        number *= number


def silly_generator():
    yield "Python"
    yield "Rocks"
    yield "So do you!"


with open('/path/to/file.txt') as fobj:
    for line in fobj:
        # process the line
        pass
