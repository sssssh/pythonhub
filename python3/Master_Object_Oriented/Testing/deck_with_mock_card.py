from suite import Suits
import random
import unittest
import unittest.mock
from card import card


class DeckEmpty(Exception):
    pass


class Deck3(list):
    def __init__(self, size=1, random=random.Random(),
                 card_factory=card):
        super().__init__()
        self.rng = random
        for d in range(size):
            super().extend(
                card_factory(r, s) for r in range(1, 13) for s in Suits)
        self.rng.shuffle(self)

    def deal(self):
        try:
            return self.pop(0)
        except IndexError:
            raise DeckEmpty()


class TestDeckBuild(unittest.TestCase):
    def setUp(self):
        self.test_card = unittest.mock.Mock(
            return_value=unittest.mock.sentinel)
        self.test_rng = random.Random()
        self.test_rng.shuffle = unittest.mock.Mock(return_value=None)

    def test_deck_1_should_build(self):
        d = Deck3(size=1, random=self.test_rng, card_factory=self.test_card)
        self.assertEqual(52*[unittest.mock.sentinel], d)
        self.test_rng.shuffle.assert_called_with(d)
        self.assertEqual(52, len(self.test_card.call_args_list))
        expected = [
            unittest.mock.call(r, s)
            for r in range(1, 14)
            for s in ('♣', '♦', '♥', '♠')]
        self.assertEqual(expected, self.test_card.call_args_list)


class TestDeckDeal(unittest.TestCase):
    def setUp(self):
        self.test_card = unittest.mock.Mock(side_effect=range(52))
        self.test_rng = random.Random()
        self.test_rng.shuffle = unittest.mock.Mock(return_value=None)

    def test_deck_1_should_deal(self):
        d = Deck3(size=1, random=self.test_rng, card_factory=self.test_card)
        dealt = []
        for c in range(52):
            c = d.deal()
            dealt.append(c)
        self.assertEqual(dealt, list(range(52)))

    def test_empty_deck_should_exception(self):
        d = Deck3(size=1, random=self.test_rng, card_factory=self.test_card)
        for c in range(52):
            c = d.deal()
        self.assertRaises(DeckEmpty, d.deal)


def suite4():
    s = unittest.TestSuite()
    s.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestDeckBuild))
    s.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestDeckDeal))
    return s


if __name__ == "__main__":
    t = unittest.TextTestRunner()
    t.run(suite4())
