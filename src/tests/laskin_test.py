import unittest
from decimal import Decimal
from services.laskin import Laskin


class TestLaskin(unittest.TestCase):
    def setUp(self):
        self.laskin = Laskin()

    def test_lisaa(self):
        self.laskin.lisaa("2")
        self.assertEqual(self.laskin.lauseke, "2")
        self.laskin.lisaa("+")
        self.laskin.lisaa("3")
        self.assertEqual(self.laskin.lauseke, "2+3")

    def test_poista_merkki(self):
        self.laskin.lisaa("2")
        self.laskin.lisaa("+")
        self.laskin.lisaa("3")
        self.laskin.poista_merkki()
        self.assertEqual(self.laskin.lauseke, "2+")

    def test_nollaa(self):
        self.laskin.lisaa("2")
        self.laskin.lisaa("+")
        self.laskin.lisaa("3")
        self.laskin.nollaa()
        self.assertEqual(self.laskin.lauseke, "")
        self.assertEqual(self.laskin.tulos, "")

    def test_laske(self):
        self.laskin.lisaa("2.1")
        self.laskin.lisaa("+")
        self.laskin.lisaa("3")
        self.laskin.laske()
        self.assertEqual(self.laskin.tulos, 5.1)
        self.assertEqual(self.laskin.lauseke, "")

    def test_virheellinen_syote(self):
        self.laskin.lisaa("2")
        self.laskin.lisaa("+")
        with self.assertRaises(Exception):
            self.laskin.laske()
