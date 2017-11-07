import unittest
from test_card import TestCard, TestAceCard, TestFaceCard


def suite2():
    s = unittest.TestSuite()
    load_from = unittest.defaultTestLoader.loadTestsFromTestCase
    s.addTests(load_from(TestCard))
    s.addTests(load_from(TestAceCard))
    s.addTests(load_from(TestFaceCard))
    return s


if __name__ == "__main__":
    t = unittest.TextTestRunner()
    t.run(suite2())
