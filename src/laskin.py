class Laskin:
    """Laskimen toiminnasta vastaava luokka."""

    def __init__(self, syote):
        """Konstruktori, joka alustaa laskimen.

        Args:
            syote (str): Laskutoimitus infix-notaatiossa.
        """
        self.syote = syote
        self.tulos = 0

    def shunting_yard(self):
        """Muuntaa infix-notaation postfix-notaatioksi shunting yard-algoritmilla.

        Returns:
            list: lauseke Postfix-notaatiossa.
        """
        postfix = []
        operaattorit = []
        luku = ""

        for merkki in self.syote:
            if merkki.isdigit():
                luku += merkki
            else:
                if luku:
                    postfix.append(luku)
                    luku = ""
                if merkki == "(":
                    operaattorit.append(merkki)
                elif merkki == ")":
                    while operaattorit[-1] != "(":
                        postfix.append(operaattorit.pop())
                    operaattorit.pop()
            if merkki in "+-*/^":
                while operaattorit and self.precedence(merkki) <= self.precedence(operaattorit[-1]):
                    postfix.append(operaattorit.pop())
                operaattorit.append(merkki)
        postfix.append(luku)
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
            float: Laskutoimituksen tulos.
        """
        postfix = self.shunting_yard()
        pino = []
        for merkki in postfix:
            if merkki.isdigit():
                pino.append(float(merkki))
            else:
                oikea = pino.pop()
                vasen = pino.pop()
                tulos = self.laskutoimitus(merkki, vasen, oikea)
                pino.append(tulos)

        self.tulos = pino.pop()
        return self.tulos

    def laskutoimitus(self, operaattori, vasen, oikea):
        """Laskee laskutoimituksen.

        Args:
            operaattori (string): Laskutoimituksen operaattori.
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
        return 0
