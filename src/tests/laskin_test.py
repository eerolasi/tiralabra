import unittest
from laskin import Laskin, VirheellinenSyote
from decimal import Decimal


class TestLaskin(unittest.TestCase):
    def setUp(self):
        self.laskin1 = Laskin("(1.5+2)-2*1/2")
        self.laskin2 = Laskin("1a2")

    def test_laskimen_syote_alustetaan_oikein(self):
        self.assertEqual(self.laskin1.syote, "(1.5+2)-2*1/2")

    def test_laskimen_tulos_alustetaan_oikein(self):
        self.assertEqual(self.laskin1.tulos, "")

    def test_tokenize_toimii(self):
        self.assertEqual(self.laskin1.tokenize(), ["(", Decimal(
            "1.5"), "+", Decimal("2"), ")", "-", Decimal("2"), "*", Decimal("1"), "/", Decimal("2")])

    def test_shunting_yard_toimii(self):
        self.assertEqual(self.laskin1.shunting_yard(), [Decimal("1.5"), Decimal(
            "2"), "+", Decimal("2"), Decimal("1"), "*", Decimal("2"), "/", "-"])
        with self.assertRaises(VirheellinenSyote):
            self.laskin2.shunting_yard()

    def test_precedence_toimii(self):
        self.assertEqual(self.laskin1.precedence("+"), 1)
        self.assertEqual(self.laskin1.precedence("-"), 1)
        self.assertEqual(self.laskin1.precedence("*"), 2)
        self.assertEqual(self.laskin1.precedence("/"), 2)
        self.assertEqual(self.laskin1.precedence("a"), 0)

    def test_laske_toimii(self):
        self.assertEqual(self.laskin1.laske(), 2.5)
