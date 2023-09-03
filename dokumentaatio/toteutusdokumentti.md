# Toteutusdokumentti

## Ohjelman yleisrakenne

- hakemistossa src sijaitseva main.py käynnistää käyttöliittymän.
- hakemistossa ui sijaitseva ui.py sisältää sovelluksen käyttöliittymän koodin.
- src/services hakemistossa sijaitsee sovelluslogiikan toteuttavat tiedostot laskin.py ja algoritmit.py 
- Luokka `Laskin` sisältää käyttöliittymän kutsumat metodit:
    - lausekkeen käsittelyä varten `lisaa(merkki)`, `poista_merkki()` ja `nollaa()`
    - `laske()` kutsuu `Algoritmit`-luokan metodia `muunna(lauseke)` muuttaakseen lausekkeen listaksi ja `laske(lista)` käynnistää algoritmien toiminnan. Metodi tuottaa poikkeuksen jos lauseke on virheellinen.

- Luokka `Algoritmit`sisältää metodit, jotka toteuttavat sovelluksen toiminnallisuudet.
    - `laske(syote)`, joka kutsuu `shunting_yard(syote)` saadakseen syötteen postfix-notaatiossa ja `laskutoimitus(merkki, vasen, oikea/None)` laskutoimituksen ratkaisemiseksi.
    - `shunting_yard(syote)` kutsuu metodia `_prioriteetti(operaattori)` lausekkeen priorisointia varten.
    - `muunna(syote)` joka muuntaa syötteen merkkijonosta listaksi.


## Puutteet ja parannusehdotukset
- Virheidenkäsittely voisi olla monipuolisempaa ja käytännöllisempää. Nyt käyttöliittymä vain ilmoittaa virheestä kun se voisi esimerkiksi estää vääränlaisen syötteen lisäämisen.
  
**Lähteet:** 
["Shunting yard algorithm", Wikipedia](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)
