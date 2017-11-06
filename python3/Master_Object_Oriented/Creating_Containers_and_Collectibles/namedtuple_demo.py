from collections import namedtuple


BlackjackCard = namedtuple('BlackjackCard', 'rank,suit,hard,soft')


def card(rank, suit):
    if rank == 1:
        return BlackjackCard('A', suit, 1, 11)
    elif 2 <= rank < 11:
        return BlackjackCard(str(rank), suit, rank, rank)
    elif rank == 11:
        return BlackjackCard('J', suit, 10, 10)
    elif rank == 12:
        return BlackjackCard('Q', suit, 10, 10)
    elif rank == 13:
        return BlackjackCard('K', suit, 10, 10)


c = card(1, '♠')
print(c)


class AceCard(BlackjackCard):
    __slots__ = ()

    def __new__(self, rank, suit):
        return super().__new__(AceCard, 'A', suit, 1, 11)


c1 = AceCard(1, '♠')
print(c1)


try:
    c1.rank = 12
    raise Exception("Shouldn't be able to set attribute.")
except AttributeError as e:
    print("Expected error:", repr(e))
