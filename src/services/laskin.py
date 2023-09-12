import re

from services.algoritmit import Algoritmit


class Laskin:
    """Luokka, joka vastaa lausekkeen käsittelystä.
    """

    def __init__(self, operaattorit, funktiot, numerot, muuttujat):
        self.lauseke = ""
        self.tulos = ""
        self.muisti = ""
        self.edellinen = ""
        self._operaattorit = operaattorit
        self._funktiot = funktiot
        self._numerot = numerot
        self._muuttujat = muuttujat
        self._algoritmit = Algoritmit(
            self._operaattorit, self._funktiot, self._numerot, self._muuttujat)

    def lisaa(self, merkki):
        """Lisää merkin lausekkeeseen.

        Args:
            merkki (str): Lisättävä merkki.
        """
        self.lauseke += str(merkki)

    def poista_merkki(self):
        """Poistaa viimeisimmän merkin tai funktion lausekkeesta.
        """
        if self.edellinen == "muisti":
            self.edellinen = ""

        if self.lauseke and self.lauseke[-1] == "(" and self.lauseke[-4:-1] in self._funktiot:
            self.lauseke = self.lauseke[:-4]
            return
        self.lauseke = self.lauseke[:-1]

    def nollaa(self):
        """Nollaa lausekkeen.
        """

        self.lauseke = ""
        self.tulos = ""
        self.edellinen = ""

    def tarkasta(self, merkki):
        """Tarkastaa voidaanko merkki lisätä lausekkeeseen.

        Args:
            merkki (str): Lisättävä merkki.
        """

        try:
            nykyinen_luku = re.findall(r"[\d.]+", self.lauseke)[-1]

        except IndexError:
            nykyinen_luku = ""

        if self.edellinen == "muisti":
            if merkki in self._numerot + self._funktiot + list(self._muuttujat) + ["("]:
                return

        if merkki not in self._operaattorit + self._funktiot + self._numerot \
                + list(self._muuttujat) + ["(", ")", "=", self.muisti]:
            return

        if self.lauseke and self.lauseke[-1] in self._numerot and merkki in \
                list(self._muuttujat) + self._funktiot + ["("]:
            return

        if self.lauseke and self.lauseke[-1] in list(self._muuttujat) and merkki in \
                list(self._muuttujat) + self._numerot + ["("]:
            return

        if merkki == ".":
            if not nykyinen_luku or "." in nykyinen_luku:
                return

        if self.lauseke and self.lauseke[-1] in self._operaattorit and merkki in self._operaattorit:
            self.poista_merkki()
            self.lisaa(merkki)
            return

        if merkki == ")" and self.lauseke.count("(") == self.lauseke.count(")"):
            return

        if not self.lauseke and merkki in ["*", "/", "^"]:
            return

        if self.lauseke and self.lauseke[-1] == ")" and merkki in self._numerot + self._funktiot \
                + list(self._muuttujat) + ["("]:
            return

        if self.lauseke and self.lauseke[-1] == "(" and merkki in "*^/)":
            return

        self.lisaa(merkki)
        self.edellinen = ""

    def tarkasta_funktio(self, funktio):
        """Tarkastaa voidaanko funktio lisätä lausekkeeseen.

        Args:
            funktio (str): Lisättävä funktio.
        """

        if not self.lauseke or self.lauseke[-1] in self._operaattorit + ["(", "="]:
            self.lisaa(funktio)
            self.lisaa("(")
            return

    def lisaa_muisti(self):
        """Lisää muistin lausekkeeseen.
        """

        if self.muisti == "":
            return

        if not self.lauseke or self.lauseke[-1] in self._operaattorit + ["(", "="]:
            self.lisaa(self.muisti)
            self.edellinen = "muisti"
            return

        self.nollaa()
        self.lisaa(self.muisti)
        self.edellinen = "muisti"
        return

    def laske(self):
        """Muuntaa lausekkeen listaksi ja laskee sen.

        Raises:
            SyntaxError: Virheellinen syöte.

        """
        if self.lauseke.count("(") != self.lauseke.count(")"):
            self.nollaa()
            raise SyntaxError("Virheellinen syöte")

        try:

            if "=" in self.lauseke:
                lista = self._algoritmit.muunna(
                    self.lauseke[self.lauseke.index("=") + 1:])
                self.tulos = round(self._algoritmit.laske(lista), 10)
                self._muuttujat[self.lauseke[self.lauseke.index(
                    "=") - 1]] = self.tulos
                self.muisti = str(self.tulos)
                self.lauseke = ""
                self.edellinen = ""
                return
            lista = self._algoritmit.muunna(self.lauseke)
            self.tulos = round(self._algoritmit.laske(lista), 10)
            self.muisti = str(self.tulos)
            self.lauseke = ""
            self.edellinen = ""
        except Exception as virhe:
            self.nollaa()
            raise SyntaxError("Virheellinen syöte") from virhe
