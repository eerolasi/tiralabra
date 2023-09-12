# Toteutusdokumentti

## Ohjelman yleisrakenne
src
├── main.py
├── services
│   ├── algoritmit.py
│   └── laskin.py
├── tests
│   ├── algoritmit_test.py
│   └── laskin_test.py
└── ui
    └── ui.py

- main.py käynnistää käyttöliittymän.
- hakemistossa ui sijaitseva ui.py sisältää sovelluksen käyttöliittymän koodin.
- services hakemistossa sijaitsee sovelluslogiikan toteuttavat tiedostot laskin.py ja algoritmit.py 
- Luokka `Laskin` tarjoaa käyttöliittymälle metodit syötteeen käsittelyyn. 
- Luokka `Algoritmit` toteuttaa laskemiseen liittyvät toiminnot.

## Puutteet ja parannusehdotukset
- Lisää funktioita
