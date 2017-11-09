from immutability import Deck


class Hand:
    def __str__(self):
        return ', '.join(map(str, self.card))

    def __repr__(self):
        return "{__class__.__name__}({dealer_card!r}, {_cards_str})".format(
            __class__=self.__class__,
            _cards_str=', '.join(map(repr, self.card)),
            **self.__dict__)

    def split(self, deck):
        """Updates this hand and also returns the new hand."""
        assert self._cards[0].rank == self._cards[1].rank
        c1 = self._cards[-1]
        del self.card
        self.card = deck.pop()
        h_new = self.__class__(self.dealer_card, c1, deck.pop())
        return h_new


class Hand_Lazy(Hand):
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self._cards = list(cards)

    @property
    def total(self):
        delta_soft = max(c.soft-c.hard for c in self._cards)
        hard_total = sum(c.hard for c in self._cards)
        if hard_total + delta_soft <= 21:
            return hard_total + delta_soft
        return hard_total

    @property
    def card(self):
        return self._cards

    @card.setter
    def card(self, aCard):
        self._cards.append(aCard)

    @card.deleter
    def card(self):
        self._cards.pop(-1)


if __name__ == '__main__':
    d = Deck()
    h = Hand_Lazy(d.pop(), d.pop(), d.pop())
    print(h.total)
    h.card = d.pop()
    print(h.total)
