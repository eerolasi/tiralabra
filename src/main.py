from laskin import Laskin

def main():
    """Sovelluksen käynnistävä metodi.
    """
    while True:
        syote = input("Anna laskutoimitus (tyhjä lopettaa): ")
        if syote == "":
            break
        laskin = Laskin(syote)
        print(laskin.laske())

if __name__ == "__main__":
    main()
