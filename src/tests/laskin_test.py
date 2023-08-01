import unittest
from laskin import Laskin
from decimal import Decimal


class TestLaskin(unittest.TestCase):
    def setUp(self):
        self.laskin = Laskin("(1.5+2)-2*1/2")

    def test_laskimen_syote_alustetaan_oikein(self):
        self.assertEqual(self.laskin.syote, "(1.5+2)-2*1/2")

    def test_laskimen_tulos_alustetaan_oikein(self):
        self.assertEqual(self.laskin.tulos, 0)

    def test_tokenize_toimii(self):
        self.assertEqual(self.laskin.tokenize(), ["(", Decimal(
            "1.5"), "+", Decimal("2"), ")", "-", Decimal("2"), "*", Decimal("1"), "/", Decimal("2")])

    def test_shunting_yard_toimii(self):
        self.assertEqual(self.laskin.shunting_yard(), [Decimal("1.5"), Decimal(
            "2"), "+", Decimal("2"), Decimal("1"), "*", Decimal("2"), "/", "-"])

    def test_precedence_toimii(self):
        self.assertEqual(self.laskin.precedence("+"), 1)
        self.assertEqual(self.laskin.precedence("-"), 1)
        self.assertEqual(self.laskin.precedence("*"), 2)
        self.assertEqual(self.laskin.precedence("/"), 2)
        self.assertEqual(self.laskin.precedence("a"), 0)

    def test_laske_toimii(self):
        self.assertEqual(self.laskin.laske(), 2.5)
