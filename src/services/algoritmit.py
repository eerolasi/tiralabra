import math


class Algoritmit:
    """Luokka, joka vastaa algoritmien toteuttamisesta.
    """

    def laske(self, syote):
        """Palauttaa laskutoimituksen tuloksen.

        Args:
            syote (str): Laskutoimitus postfix-notaatiossa.

        Returns:
            float: Laskutoimituksen tulos.
        """
        postfix = self._shunting_yard(syote)
        pino = []
        for merkki in postfix:
            if isinstance(merkki, (int, float)):
                pino.append(merkki)
            elif merkki in ["+", "-", "*", "/", "^"]:
                oikea = pino.pop()
                vasen = pino.pop()
                pino.append(self._laskutoimitus(merkki, vasen, oikea))
            elif merkki in ["s", "c", "t", "√"]:
                luku = pino.pop()
                pino.append(self._laskutoimitus(merkki, luku, None))
        return pino.pop()

    def _shunting_yard(self, syote):
        """Palauttaa laskutoimituksen merkit muunnettuna infix-notaatiosta postfix-notaatioon.

        Args:
            syote (str): Laskutoimitus infix-notaatiossa.

        Returns:
            list: Laskutoimitus postfix-notaatiossa.
        """

        postfix = []
        operaattorit = []
        for merkki in syote:
            if isinstance(merkki, float):
                postfix.append(merkki)
            elif merkki in ["s", "c", "t", "√"]:
                operaattorit.append(merkki)
            elif merkki in ["+", "-", "*", "/", "^"]:
                while operaattorit and self._prioriteetti(merkki) \
                        <= self._prioriteetti(operaattorit[-1]):
                    postfix.append(operaattorit.pop())
                operaattorit.append(merkki)
            elif merkki == "(":
                operaattorit.append(merkki)
            elif merkki == ")":
                while operaattorit[-1] != "(":
                    postfix.append(operaattorit.pop())
                operaattorit.pop()

        while operaattorit:
            postfix.append(operaattorit.pop())
        return postfix

    def _prioriteetti(self, operaattori):
        """Palauttaa operaattorin prioriteetin.

        Args:
            operaattori (str): Laskutoimituksen operaattori.
        Returns:
            int: Operaattorin prioriteetti.
        """

        prioriteetit = {"+": 1, "-": 1, "*": 2, "/": 2,
                        "^": 3, "s": 4, "c": 4, "t": 4, "√": 4}
        return prioriteetit.get(operaattori, 0)

    def _laskutoimitus(self, operaattori, vasen, oikea):
        """Palauttaa laskutoimituksen tuloksen.

        Args:
            operaattori (str): Laskutoimituksen operaattori.
            vasen (float): Laskutoimituksen vasen operandi.
            oikea (float): Laskutoimituksen oikea operandi.
        Returns:
            float: Laskutoimituksen tulos.
        """

        if operaattori == "+":
            return vasen + oikea
        elif operaattori == "-":
            return vasen - oikea
        elif operaattori == "*":
            return vasen * oikea
        elif operaattori == "/":
            return vasen / oikea
        elif operaattori == "^":
            return vasen ** oikea
        elif operaattori == "s":
            return math.sin(vasen)
        elif operaattori == "c":
            return math.cos(vasen)
        elif operaattori == "t":
            return math.tan(vasen)
        elif operaattori == "√":
            return math.sqrt(vasen)

    def muunna(self, syote):
        """Palauttaa syötteen merkit muunnettuna merkkijonosta listaksi.

        Args:
            syote (str): Laskutoimitus merkkijonona.

        Returns:
            list: Laskutoimitus listana.
        """

        merkit = []
        luku = ""
        edellinen = ""
        for merkki in syote:
            if merkki.isdigit():
                luku += merkki
            elif merkki == ".":
                luku += merkki
            elif luku:
                merkit.append(float(luku))
                luku = ""
                merkit.append(merkki)
            elif merkki == "-" and (not merkit or merkit[-1] in ["+", "-", "*", "/", "^", "("]):
                merkit.append(0.0)
                merkit.append(merkki)

            elif merkki in "sct√":
                if merkki == "s" and edellinen == "o":
                    continue
                merkit.append(merkki)
            elif merkki in "+-*/^()":
                merkit.append(merkki)
            edellinen = merkki

        if luku:
            merkit.append(float(luku))
        return merkit
