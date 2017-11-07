import unittest
from card import Card, AceCard, FaceCard


class TestCard(unittest.TestCase):
    def setUp(self):
        self.three_clubs = Card(3, '♣')

    def test_should_returnStr(self):
        self.assertEqual("3♣", str(self.three_clubs))

    def test_should_getAttrValues(self):
        self.assertEqual(3, self.three_clubs.rank)
        self.assertEqual("♣", self.three_clubs.suit)
        self.assertEqual(3, self.three_clubs.hard)
        self.assertEqual(3, self.three_clubs.soft)


class TestAceCard(unittest.TestCard):
    def setUp(self):
        self.ace_spades = AceCard(1, '♠')

    def test_should_returnStr(self):
        self.assertEqual("A♠", str(self.ace_spades))

    def test_should_getAttrValues(self):
        self.assertEqual(1, self.ace_spades.rank)
        self.assertEqual("♠", self.ace_spades.suit)
        self.assertEqual(1, self.ace_spades.hard)
        self.assertEqual(11, self.ace_spades.soft)


class TestFaceCard(unittest.TestCase):
    def setUp(self):
        self.queen_hearts = FaceCard(12, '♥')

    def test_should_returnStr(self):
        self.assertEqual("Q♥", str(self.queen_hearts))

    def test_should_getAttrValues(self):
        self.assertEqual(12, self.queen_hearts.rank)
        self.assertEqual("♥", self.queen_hearts.suit)
        self.assertEqual(10, self.queen_hearts.hard)
        self.assertEqual(10, self.queen_hearts.soft)
