class City(str):
    def __hash__(self):
        return ord(self[0])


if __name__ == '__main__':
    data = {
        City("Rome"),
        City("San Francisco"),
        City("New York"),
        City("Barcelona"),
    }
    print(data)
