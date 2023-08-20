import tkinter as ttk
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
        self._syote = None
        self._laskin = Laskin()
        self._operaattorit = ["+", "-", "*", "/", "(", ")", "^"]
        self._numerot = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"]

    def start(self):
        """Käynnistää käyttöliittymän."""
        self._syote = ttk.Entry(self._root)
        self._syote.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

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

        ttk.Button(self._root, text=".", command=lambda i=i: self._lisaa(".")).grid(
            row=4, column=1, padx=5, pady=5
        )

        ttk.Button(self._root, text="C", command=self._nollaa).grid(
            row=4, column=2, padx=5, pady=5
        )

        ttk.Button(self._root, text="=", command=self._laske).grid(
            row=4, column=4, padx=5, pady=5
        )

        ttk.Button(self._root, text="del", command=self._poista).grid(
            row=5, column=2, padx=5, pady=5
        )

        ttk.Button(self._root, text="+/-", command=self._vaihda_etumerkki).grid(
            row=5, column=0, padx=5, pady=5
        )

    def _lisaa(self, merkki):
        """Lisää merkin syötteeseen.

        Args:
            merkki (str): Lisättävä merkki.
        """
        if self._syote.get() == "Error":
            self._syote.delete(0, ttk.END)

        self._syote.insert(ttk.END, merkki)

    def _vaihda_etumerkki(self):
        """Vaihtaa luvun etumerkin."""
        syote = self._syote.get()

        if syote and syote[0] == "-":
            self._syote.delete(0)
        else:
            self._syote.insert(0, "-")

    def _laske(self):
        """Laskee laskutoimituksen tuloksen.
        """

        try:
            tulos = self._laskin.laske(self._syote.get())
            self._syote.delete(0, ttk.END)
            self._syote.insert(ttk.END, tulos)
        except ValueError:
            self._syote.delete(0, ttk.END)
            self._syote.insert(ttk.END, "Error")

    def _poista(self):
        """Poistaa syötteen viimeisen merkin.
        """
        self._syote.delete(len(self._syote.get()) - 1, ttk.END)

    def _nollaa(self):
        """Nollaa syötteen.
        """
        self._syote.delete(0, ttk.END)
