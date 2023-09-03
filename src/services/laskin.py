from services.algoritmit import Algoritmit


class Laskin:
    """Luokka, joka vastaa lausekkeen käsittelystä.
    """

    def __init__(self):
        self.lauseke = ""
        self.tulos = ""
        self._algoritmit = Algoritmit()

    def lisaa(self, merkki):
        """Lisää merkin lausekkeeseen.
        Args:
            merkki (str): Lisättävä merkki.
        """
        self.lauseke += str(merkki)

    def poista_merkki(self):
        """Poistaa viimeisimmän merkin lausekkeesta.
        """

        self.lauseke = self.lauseke[:-1]

    def nollaa(self):
        """Nollaa lausekkeen ja tuloksen.
        """

        self.lauseke = ""
        self.tulos = ""

    def laske(self):
        """Muuntaa lausekkeen listaksi ja laskee sen.

        Raises:
            SyntaxError: Virheellinen syöte.
        """

        try:
            lista = self._algoritmit.muunna(self.lauseke)
            self.tulos = round(self._algoritmit.laske(lista), 10)
            self.lauseke = ""
        except Exception as virhe:
            self.nollaa()
            raise SyntaxError("Virheellinen syöte") from virhe
