from decimal import Decimal


class Laskin:
    """Laskimen toiminnasta vastaava luokka."""

    def __init__(self, syote):
        """Konstruktori, joka alustaa laskimen.

        Args:
            syote (str): Laskutoimitus infix-notaatiossa.
        """
        self.syote = syote
        self.tulos = 0

    def tokenize(self):
        """Palauttaa laskutoimituksksen merkit listana, jossa luvut on muunnettu desimaaliluvuiksi.

        Returns:
            list: Laskutoimituksen merkit listana.
        """
        merkit = []
        luku = ""

        for merkki in self.syote:
            if merkki.isdigit():
                luku += merkki
            elif merkki == ".":
                luku += merkki
            else:
                if luku:
                    merkit.append(Decimal(luku))
                    luku = ""
                merkit.append(merkki)
        if luku:
            merkit.append(Decimal(luku))
        return merkit

    def shunting_yard(self):
        """Palauttaa laskutoimituksen merkit muunnettuna infix-notaatiosta postfix-notaatioon.

        Returns:
            list: Laskutoimituksen merkit listana.
        """
        postfix = []
        operaattorit = []
        syote_lista = self.tokenize()
        for merkki in syote_lista:
            if isinstance(merkki, Decimal):
                postfix.append(merkki)
            elif merkki == "(":
                operaattorit.append(merkki)
            elif merkki == ")":
                while operaattorit[-1] != "(":
                    postfix.append(operaattorit.pop())
                operaattorit.pop()
            elif merkki in "+-*/":
                while operaattorit \
                        and self.precedence(merkki) <= self.precedence(operaattorit[-1]):
                    postfix.append(operaattorit.pop())
                operaattorit.append(merkki)
        while operaattorit:
            postfix.append(operaattorit.pop())
        return postfix

    def precedence(self, operaattori):
        """Palauttaa operaattorin prioriteetin.

        Args:
            operaattori (str): Laskutoimituksen operaattori.

        Returns:
            int: Operaattorin prioriteetti.
        """
        prioriteetit = {"+": 1, "-": 1, "*": 2, "/": 2}
        return prioriteetit.get(operaattori, 0)

    def laske(self):
        """Palauttaa laskutoimituksen tuloksen.

        Returns:
            Decimal: Laskutoimituksen tulos.
        """
        postfix = self.shunting_yard()
        pino = []
        for merkki in postfix:
            if isinstance(merkki, Decimal):
                pino.append(merkki)
            else:
                oikea = pino.pop()
                vasen = pino.pop()
                tulos = self.laskutoimitus(merkki, vasen, oikea)
                pino.append(tulos)

        self.tulos = pino.pop()
        return self.tulos

    def laskutoimitus(self, operaattori, vasen, oikea):
        """Palauttaa laskutoimituksen tuloksen.

        Args:
            operaattori (string): Laskutoimituksen operaattori.
            vasen (Decimal): Laskutoimituksen vasen operandi.
            oikea (Decimal): Laskutoimituksen oikea operandi.

        Returns:
            Decimal: Laskutoimituksen tulos.
        """
        if operaattori == "+":
            return vasen + oikea
        if operaattori == "-":
            return vasen - oikea
        if operaattori == "*":
            return vasen * oikea
        if operaattori == "/":
            return vasen / oikea
        return 0
