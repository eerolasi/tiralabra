import tkinter as ttk
from math import pi

from services.laskin import Laskin


class UI:
    """Käyttöliittymästä vastaava luokka.
    """

    def __init__(self, root):
        """Konstruktori, joka alustaa käyttöliittymän.

        Args:
            root (tkinter.Tk): Käyttöliittymän juuri.
        """
        self._root = root
        self._syote = ttk.StringVar()
        self._laskin = Laskin()
        self._operaattorit = ["+", "-", "*", "/", "^"]
        self._funktiot = ["sin", "cos", "tan", "√"]
        self._numerot = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", "."]

    def kaynnista(self):
        """Alustaa käyttöliittymän näkymän.
        """
        self._syote.set("")
        ttk.Label(self._root, textvariable=self._syote).grid(
            row=0, column=0, columnspan=6, padx=5, pady=5
        )
        self._root.bind("<Return>", lambda event: self._laske())
        self._root.bind("<BackSpace>", lambda event: self._poista_merkki())
        self._root.bind("<Delete>", lambda event: self._nollaa())
        self._root.bind("<Escape>", lambda event: self._root.destroy())
        self._root.bind("<Key>", lambda event: self._lisaa(event.char))
        for i in self._numerot:
            ttk.Button(self._root, text=i, command=lambda i=i: self._lisaa(i)).grid(
                row=self._numerot.index(i) // 3 + 1,
                column=self._numerot.index(i) % 3,
                padx=5,
                pady=5,
            )

        for i in self._operaattorit:
            ttk.Button(self._root, text=i, command=lambda i=i: self._lisaa(i)).grid(
                row=self._operaattorit.index(i) // 2 + 1,
                column=self._operaattorit.index(i) % 2 + 3,
                padx=5,
                pady=5,
            )

        for i in self._funktiot:
            ttk.Button(self._root, text=i, command=lambda i=i: self._lisaa_funktio(i)).grid(
                row=self._funktiot.index(i) + 1,
                column=5,
                padx=5,
                pady=5,
            )

        ttk.Button(self._root, text="(", command=lambda i=i: self._lisaa("(")).grid(
            row=3, column=4, padx=5, pady=5
        )

        ttk.Button(self._root, text=")", command=lambda i=i: self._lisaa(")")).grid(
            row=4, column=4, padx=5, pady=5
        )

        ttk.Button(self._root, text=".", command=lambda i=i: self._lisaa(".")).grid(
            row=4, column=1, padx=5, pady=5
        )

        ttk.Button(self._root, text="AC", command=self._nollaa).grid(
            row=4, column=2, padx=5, pady=5
        )

        ttk.Button(self._root, text="=", command=self._laske).grid(
            row=5, column=4, padx=5, pady=5
        )

        ttk.Button(self._root, text="π", command=lambda i=i: self._lisaa(pi)).grid(
            row=5, column=0, padx=5, pady=5
        )

        ttk.Button(self._root, text="C", command=self._poista_merkki).grid(
            row=4, column=3, padx=5, pady=5
        )

    def _lisaa(self, merkki):
        """Lisää merkin syötekenttään.

        Args:
            merkki (str): Lisättävä merkki.
        """
        if merkki == "=":
            self._laske()
            return

        try:

            self._laskin.lisaa(merkki)

            self._syote.set(self._laskin.lauseke)

        except SyntaxError:
            self._syote.set("Virheellinen syöte")

    def _lisaa_funktio(self, funktio):
        """Lisää funktion syötekenttään.

        Args:
            funktio (str): Lisättävä funktio.
        """

        try:
            self._laskin.lisaa(funktio)
            self._laskin.lisaa("(")
            self._syote.set(self._laskin.lauseke)

        except SyntaxError:
            self._syote.set("Virheellinen syöte")

    def _laske(self):
        """Laskee syötekentässä olevan lausekkeen.
        """

        try:
            self._laskin.laske()
            self._syote.set(self._laskin.tulos)
        except SyntaxError:
            self._syote.set("Virheellinen syöte")

    def _nollaa(self):
        """Nollaa syötekentän.
        """

        self._laskin.nollaa()
        self._syote.set(self._laskin.lauseke)

    def _poista_merkki(self):
        """Poistaa viimeisimmän merkin syötekentästä.
        """

        self._laskin.poista_merkki()
        self._syote.set(self._laskin.lauseke)
