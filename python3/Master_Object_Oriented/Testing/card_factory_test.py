import unittest
from card import Card, AceCard, card, LogicError


class TestCardFactory(unittest.TestCase):
    def test_rank1_shuold_createAceCard(self):
        c = card(1, '♣')
        self.assertIsInstance(c, AceCard)

    def test_rank2_should_createCard(self):
        c = card(2, '♦')
        self.assertIsInstance(c, Card)

    def test_rank10_should_createCard(self):
        c = card(10, '♥')
        self.assertIsInstance(c, Card)

    def test_rank13_should_createFaceCard(self):
        c = card(13, '♣')
        self.assertIsInstance(c, Card)

    def test_otherRank_should_exception(self):
        with self.assertRaises(LogicError):
            c = card(14, '♦')
        with self.assertRaises(LogicError):
            c = card(0, '♦')


def suite3():
    s = unittest.TestSuite()
    s.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestCardFactory))
    return s


if __name__ == "__main__":
    t = unittest.TextTestRunner()
    t.run(suite3())
