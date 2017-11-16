import sys


def card(rank, suit):
    """Create a ``Card``instance from rank and suit.

    :param suit: Suit object (often a character from '♣♡♢♠')
    :param rank: Numeric rank in the range 1-13.
    :returns: Card instance
    :raises TypeError: rank out of range.
    >>> import sphinx-style_documentation.py
    >>> sphinx-style_documentation.card(3, '♡')
    """
    if rank == 1:
        return AceCard(rank, suit, 1, 11)
    elif 2 <= rank < 11:
        return Card(rank, suit, rank)
    elif 11 <= rank < 14:
        return FaceCard(rank, suit, 10)
    else:
        raise TypeError



class Card:
    """Definition of a number rank playing card.
    Subclasses will define ``FaceCard`` and ``AceCard``.

    :ivar rank: Rank
    :ivar suit: Suit
    :ivar hard: Hard point total for a card
    :ivar soft: Soft total; same as hard for all cards except Aces.
    """
    def __init__(self, rank, suit, hard, soft=None):
        """Define the values for this card.

        :param rank: Numeric rank in the range 1-13.
        :param suit: Suit object (often a character from '♣♡♢♠')
        :param hard: Hard point total (or 10 for FaceCard or 1 for AceCard)
        :param soft: The soft total for AceCard, otherwise defaults to hard.
        """
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft if soft is not None else hard

    def __repr__(self):
        return "{rank}{suit}".format(**self.__dict__)
