from tkinter import Tk
from ui.ui import UI


def main():
    """Sovelluksen käynnistävä metodi.
    """
    window = Tk()
    window.title("Laskin")
    ui = UI(window)
    ui.kaynnista()
    window.mainloop()


if __name__ == "__main__":
    main()
