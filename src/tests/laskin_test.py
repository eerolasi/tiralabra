import unittest
from decimal import Decimal
from services.laskin import Laskin


class TestLaskin(unittest.TestCase):
    def setUp(self):
        self._operaattorit = ["+", "-", "*", "/", "^"]
        self._funktiot = ["sin", "cos", "tan", "√"]
        self._numerot = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", "."]
        self._muuttujat = {"x": None, "y": None, "z": None}
        self.laskin = Laskin(self._operaattorit, self._funktiot,
                             self._numerot, self._muuttujat)
        self.laskin.lauseke = ""
        self.laskin.muisti = ""

    def test_tarkasta(self):
        self.laskin.lauseke = ""
        self.laskin.tarkasta("*")
        self.assertEqual(self.laskin.lauseke, "")
        self.laskin.tarkasta("1")
        self.assertEqual(self.laskin.lauseke, "1")
        self.laskin.tarkasta("'")
        self.assertEqual(self.laskin.lauseke, "1")
        self.laskin.tarkasta(".")
        self.laskin.tarkasta(".")
        self.assertEqual(self.laskin.lauseke, "1.")

        self.laskin.lauseke = ""
        self.laskin.tarkasta("(")
        self.laskin.tarkasta(")")
        self.assertEqual(self.laskin.lauseke, "(")
        self.laskin.tarkasta("1")
        self.laskin.tarkasta(")")
        self.laskin.tarkasta(")")
        self.assertEqual(self.laskin.lauseke, "(1)")
        self.laskin.tarkasta("3")
        self.assertEqual(self.laskin.lauseke, "(1)")

        self.laskin.edellinen = "muisti"
        self.laskin.tarkasta("1")
        self.assertEqual(self.laskin.lauseke, "(1)")

        self.laskin.lauseke = "y"
        self.laskin.tarkasta("x")
        self.assertEqual(self.laskin.lauseke, "y")
        self.laskin.tarkasta("(")
        self.assertEqual(self.laskin.lauseke, "y")
        self.laskin.tarkasta("+")
        self.laskin.tarkasta("-")
        self.assertEqual(self.laskin.lauseke, "y-")

        self.laskin.lauseke = ""
        self.laskin.tarkasta("3")
        self.laskin.tarkasta("(")
        self.assertEqual(self.laskin.lauseke, "3")

    def test_tarkasta_funktio(self):

        self.laskin.tarkasta_funktio("sin")
        self.assertEqual(self.laskin.lauseke, "sin(")
        self.laskin.lauseke = ""
        self.laskin.tarkasta("1")
        self.laskin.tarkasta_funktio("sin")
        self.assertEqual(self.laskin.lauseke, "1")

    def test_lisaa_muisti(self):
        self.laskin.muisti = ""
        self.laskin.lisaa_muisti()
        self.assertEqual(self.laskin.muisti, "")
        self.laskin.muisti = "3"
        self.laskin.lisaa_muisti()
        self.assertEqual(self.laskin.lauseke, "3")
        self.laskin.tarkasta("/")
        self.laskin.lisaa_muisti()
        self.assertEqual(self.laskin.lauseke, "3/3")
        self.laskin.lisaa_muisti()
        self.assertEqual(self.laskin.lauseke, "3")

    def test_laske(self):
        self.laskin.lauseke = "("

        with self.assertRaises(SyntaxError):
            self.laskin.laske()

        self.laskin.lauseke = "y=2+3"
        self.laskin.laske()
        self.assertEqual(self.laskin._muuttujat["y"], 5.0)

        self.laskin.lauseke = "4/2-1"
        self.laskin.laske()
        self.assertEqual(self.laskin.tulos, 1.0)

        self.laskin.lauseke = "8+"
        with self.assertRaises(SyntaxError):
            self.laskin.laske()

    def test_poista_merkki(self):
        self.laskin.edellinen = "muisti"
        self.laskin.poista_merkki()
        self.assertEqual(self.laskin.edellinen, "")
        self.laskin.lauseke = "1+"
        self.laskin.poista_merkki()
        self.assertEqual(self.laskin.lauseke, "1")
        self.laskin.lauseke = "sin("
        self.laskin.poista_merkki()
        self.assertEqual(self.laskin.lauseke, "")
