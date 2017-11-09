import random


__all__ = ['RateTimeDistance']


class BlackJackCard:
    '''Abstrac Superclass'''
    __slots__ = ('rank', 'suit', 'hard', 'soft')

    def __init__(self, rank, suit, hard, soft):
        super().__setattr__('rank', rank)
        super().__setattr__('suit', suit)
        super().__setattr__('hard', hard)
        super().__setattr__('soft', soft)

    def __str__(self):
        return "{0.rank}{0.suit}".format(self)

    def __setattr__(self, name, value):
        raise AttributeError("'{__class__.__name__}' has no attribute '{name}'".format(
            __class__=self.__class__, name=name))

    def __lt__(self, other):
        if not isinstance(other, BlackJackCard):
            return NotImplemented
        return self.rank < other.rank

    def __le__(self, other):
        try:
            return self.rank <= other.rank
        except AttributeError:
            return NotImplemented

    def __gt__(self, other):
        if not isinstance(other, BlackJackCard):
            return NotImplemented
        return self.rank > other.rank

    def __ge__(self, other):
        if not isinstance(other, BlackJackCard):
            return NotImplemented
        return self.rank >= other.rank

    def __eq__(self, other):
        if not isinstance(other, BlackJackCard):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    def __ne__(self, other):
        if not isinstance(other, BlackJackCard):
            return NotImplemented
        return self.rank != other.rank and self.suit == other.suit


class Ace21Card(BlackJackCard):
    def __init__(self, rank, suit):
        super().__init__("A", suit, 1, 11)


class Face21Card(BlackJackCard):
    def __init__(self, rank, suit):
        super().__init__({11: 'J', 12: 'Q', 13: 'K'}[rank], suit, 10, 10)


class Number21Card(BlackJackCard):
    def __init__(self, rank, suit):
        super().__init__(str(rank), suit, rank, rank)


def card21(rank, suit):
    if rank == 1:
        return Ace21Card(rank, suit)
    elif 2 <= rank < 11:
        return Number21Card(rank, suit)
    elif 11 <= rank < 14:
        return Face21Card(rank, suit)
    else:
        raise TypeError


Suits = '♣', '♦', '♥', '♠'


class Deck(list):
    def __init__(self, decks=6, factory=card21):
        super().__init__()
        for i in range(decks):
            self.extend(factory(r+1, s) for r in range(13) for s in Suits)
        random.shuffle(self)
        burn = random.randint(1, 52)
        for i in range(burn):
            self.pop()


class BlackJackCard2(tuple):
    """Abstract Superclass"""
    def __new__(cls, rank, suit, hard, soft):
        return super().__new__(cls, (rank, suit, hard, soft))

    def __getattr__(self, name):
        return self[{'rank': 0, 'suit': 1, 'hard': 2, 'soft': 3}[name]]

    def __setattr__(self, name, value):
        raise NotImplemented


class BlackJackCard3:
    """Abstract Superclass"""
    def __init__(self, rank, suit, hard, soft):
        super().__setattr__('rank', rank)
        super().__setattr__('suit', suit)
        super().__setattr__('hard', hard)
        super().__setattr__('soft', soft)

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError("Cannot set {name}".format(name=name))
        raise AttributeError("'{__class__.__name__}' has no attribute '{name}'".format(
            __class__=self.__class__, name=name))

    def __getattribute__(self, name):
        if name.startswith('_'):
            raise AttributeError
        return object.__getattribute__(self, name)


c = BlackJackCard3("A", '♠', 1, 11)

card2d = card21(2, '♦')
card2s = card21(2, '♠')
card3d = card21(3, '♦')


def compare(a, b):
    print(a, b, ':', '==', a == b, '<', a < b, '<=', a <= b)


compare(card2d, card2s)
compare(card2s, card3d)
try:
    compare(card2d, 2)
except TypeError as e:
    print("Expected", e)
