
import unittest
from services.algoritmit import Algoritmit


class TestAlgoritmit(unittest.TestCase):
    def setUp(self):
        self._operaattorit = ["+", "-", "*", "/", "^"]
        self._funktiot = ["sin", "cos", "tan", "√"]
        self._numerot = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", "."]
        self._muuttujat = {"x": None, "y": None, "z": 2.0}
        self.algoritmit = Algoritmit(self._operaattorit, self._funktiot,
                                     self._numerot, self._muuttujat)

        self.syote = "1-2+3*4/2^2+√(9)"
        self.syote2 = "-sin(9+9)+cos(1-2)+tan(3)"
        self.syote3 = "z+3.1"
        self.syote4 = "x+2"
        self.syote5 = "1--2"

    def test_muunna(self):
        self.syote = self.algoritmit.muunna(self.syote)
        self.assertEqual(self.syote, [
                         1.0, "-", 2.0, "+", 3.0, "*", 4.0, "/", 2.0, "^", 2.0, "+", "√", "(", 9.0, ")"])

        self.syote2 = self.algoritmit.muunna(self.syote2)
        self.assertEqual(self.syote2, [0.0, "-", "sin", "(", 9.0, "+", 9.0, ")",
                         "+", "cos", "(", 1.0, "-", 2.0, ")", "+", "tan", "(", 3.0, ")"])

        self.syote3 = self.algoritmit.muunna(self.syote3)
        self.assertEqual(self.syote3, [2.0, "+", 3.1])

        self.syote4 = self.algoritmit.muunna(self.syote4)
        self.assertEqual(self.syote4, None)

        self.syote5 = self.algoritmit.muunna(self.syote5)
        self.assertEqual(self.syote5, [1.0, "+", 2.0])

    def test_laske(self):
        self.syote = self.algoritmit.muunna(self.syote)
        tulos = self.algoritmit.laske(self.syote)
        self.assertEqual(tulos, 5.0)

        self.syote2 = self.algoritmit.muunna(self.syote2)
        tulos2 = self.algoritmit.laske(self.syote2)
        self.assertEqual(round(tulos2, 10), 1.1487430096)

        self.syote3 = self.algoritmit.muunna(self.syote3)
        tulos3 = self.algoritmit.laske(self.syote3)
        self.assertEqual(round(tulos3, 10), 5.1)
