
import unittest
from services.algoritmit import Algoritmit


class TestAlgoritmit(unittest.TestCase):
    def setUp(self):
        self.algoritmit = Algoritmit()
        self.syote = "1-2+3*4/2^2+√(9)"
        self.syote = self.algoritmit.muunna(self.syote)
        self.syote2 = "sin(9+9)+cos(1-2)"
        self.syote2 = self.algoritmit.muunna(self.syote2)
        self.syote3 = "-3+tan(3.0)"
        self.syote3 = self.algoritmit.muunna(self.syote3)

    def test_shunting_yard(self):
        postfix = self.algoritmit._shunting_yard(self.syote)
        self.assertEqual(
            postfix, [1, 2, "-", 3, 4, "*", 2, 2, "^", "/", "+", 9, "√", "+"])
        postfix2 = self.algoritmit._shunting_yard(self.syote2)
        self.assertEqual(postfix2, [9, 9, "+", "s", 1, 2, "-", "c", "+"])
        postfix3 = self.algoritmit._shunting_yard(self.syote3)
        self.assertEqual(postfix3, [0, 3, "-", 3, "t", "+"])

    def test_laske(self):
        tulos = self.algoritmit.laske(self.syote)
        self.assertEqual(tulos, 5)
        tulos2 = self.algoritmit.laske(self.syote2)
        self.assertEqual(tulos2, -0.2106849409035364)
        tulos3 = self.algoritmit.laske(self.syote3)
        self.assertEqual(tulos3, -3.1425465430742777)
