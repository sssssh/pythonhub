import random
from collections import namedtuple, deque


card = namedtuple('card', 'rank,suit')
Suits = '♣', '♦', '♥', '♠'


class Deck(deque):
    def __init__(self, size=1):
        super().__init__()
        for d in range(size):
            cards = [card(r, s) for r in range(13) for s in Suits]
            super().extend(cards)
        random.shuffle(self)


d = Deck()
print(d)
print(d.pop(), d.pop(), d.pop())
