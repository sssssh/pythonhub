import random


Suits = '♣', '♦', '♥', '♠'


class Card:
    def __init__(self, rank, suit, hard=None, soft=None):
        self.rank = rank
        self.suit = suit
        self.hard = hard or int(rank)
        self.soft = soft or int(rank)

    def __str__(self):
        return "{0.rank!s}{0.suit!s}".format(self)


class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__(rank, suit, 1, 11)


class FaceCard(Card):
    def __init__(self, rank, suit):
        super().__init__(rank, suit, 10, 10)


class LogicError(Exception):
    pass


def card(rank, suit):
    if rank == 1:
        return AceCard(rank, suit)
    elif 2 <= rank < 11:
        return Card(rank, suit)
    elif 11 <= rank < 14:
        return FaceCard(rank, suit)
    else:
        raise Exception("LogicError")


class Deck1(list):
    def __init__(self, size=1):
        super().__init__()
        self.rng = random.Random()
        for d in range(size):
            for s in Suits:
                cards = ([AceCard(1, s)]
                         + [Card(r, s) for r in range(2, 12)]
                         + [FaceCard(r, s) for r in range(12, 14)])
                super().extend(cards)
        self.rng.shuffle(self)


class Deck2(list):
    def __init__(self, size=1,
                 random=random.Random(),ace_class=AceCard,
                 card_class=Card, face_class=FaceCard):
        super().__init__()
        self.rng = random
        for d in range(size):
            for s in Suits:
                cards = ([ace_class(1, s)]
                         + [card_class(r, s) for r in range(2, 12)]
                         + [face_class(r, s) for r in range(12, 14)])
                super().extend(cards)
        self.rng.shuffle(self)

