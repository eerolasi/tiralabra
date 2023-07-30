import unittest
from laskin import Laskin


class TestLaskin(unittest.TestCase):
    def setUp(self):
        self.laskin = Laskin("(1+2)-2*1/2")

    def test_laskimen_syote_alustetaan_oikein(self):
        self.assertEqual(self.laskin.syote, "(1+2)-2*1/2")

    def test_laskimen_tulos_alustetaan_oikein(self):
        self.assertEqual(self.laskin.tulos, 0)

    def test_shunting_yard_toimii(self):
        self.assertEqual(self.laskin.shunting_yard(), [
                         "1", "2", "+", "2", "1", "*", "2", "/", "-"])

    def test_precedence_toimii(self):
        self.assertEqual(self.laskin.precedence("+"), 1)
        self.assertEqual(self.laskin.precedence("-"), 1)
        self.assertEqual(self.laskin.precedence("*"), 2)
        self.assertEqual(self.laskin.precedence("/"), 2)
        self.assertEqual(self.laskin.precedence("a"), 0)

    def test_laske_toimii(self):
        self.assertEqual(self.laskin.laske(), 2)
