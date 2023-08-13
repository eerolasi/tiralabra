import unittest
from services.laskin import Laskin
from decimal import Decimal


class TestLaskin(unittest.TestCase):
    def setUp(self):
        self.laskin = Laskin()
        self.syote = "(1.5+2)-2*1/2"
        self.syote2 = "3^3"

    def test_laskimen_tulos_alustetaan_oikein(self):
        self.assertEqual(self.laskin._tulos, None)

    def test_tokenize_toimii(self):
        self.assertEqual(self.laskin.tokenize(self.syote), ["(", Decimal(
            "1.5"), "+", Decimal("2"), ")", "-", Decimal("2"), "*", Decimal("1"), "/", Decimal("2")])

    def test_shunting_yard_toimii(self):
        self.assertEqual(self.laskin.shunting_yard(self.syote), [Decimal("1.5"), Decimal(
            "2"), "+", Decimal("2"), Decimal("1"), "*", Decimal("2"), "/", "-"])

    def test_precedence_toimii(self):
        self.assertEqual(self.laskin.precedence("^"), 3)
        self.assertEqual(self.laskin.precedence("*"), 2)
        self.assertEqual(self.laskin.precedence("/"), 2)
        self.assertEqual(self.laskin.precedence("+"), 1)
        self.assertEqual(self.laskin.precedence("-"), 1)

    def test_laskin_laskee_oikein(self):
        self.assertEqual(self.laskin.laske(self.syote), 2.5)
        self.assertEqual(self.laskin.laske(self.syote2), 27)
