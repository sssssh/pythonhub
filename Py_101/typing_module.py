# type hinting
def some_function(number: int, name: str) -> None:
    print("%s entered %s" % (name, number))


def process_data(my_list: list, name: str) -> bool:
    return name in my_list


class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color


def salad(fruit_one: Fruit, fruit_two: Fruit) -> list:
    print(fruit_one.name)
    print(fruit_two.name)
    return [fruit_one, fruit_two]


Animal = str


def zoo(animal: Animal, number: int) -> None:
    print("The zoo has %s %s" % (number, animal))
