# Käyttöohje

## Python-versio
- 3.11

## Käynnistä virtuaaliympäristö juurihakemistosta
````
poetry shell
````

## Asenna riippuvuudet
````
poetry install
````

### Ohjelman suorittaminen
````
poetry run invoke run
````
![laskutoimitus](https://github.com/eerolasi/tiralabra/blob/main/dokumentaatio/laskutoimitus.png)

![laskutoimitus](https://github.com/eerolasi/tiralabra/blob/main/dokumentaatio/tulos.png)


## Syötteet
- Syötteen voi antaa sekä käyttöliittymän painikkeiden kautta että näppäimistöllä.

## Laskutoimituksen suoritus
- Enteriä painamalla
- `=`-merkkiä painamalla näppäimistöstä tai käyttöliittymästä.

## Arvon sijoittaminen muuttujaan
- Käytettävissä muuttujat `y, x, z`
- Esim. `y=2+2` asettaa `y`:n arvoksi `4.0`
- Kun muuttujaa määritellään eli ensimmäinen merkki on muuttuja ja seuraava yhtäsuuruusmerkki, ei ensimmäinen `=`-merkki edellä mainittuun tapaan suorita laskutoimitusta. Seuraava yhtäsuuruusmerkin painallus asettaa arvon muuttujaan.
- Arvon asettamisen jälkeen muuttujia voidaan käyttää muiden syötteiden tapaan lausekkeen osana.
- esim. `y+4=8`

## Muisti
- Tulos tallentuu automaattisesti muistiin laskutoimituksen suorituksen yhteydessä.
- `Ans`-painikketta painamalla saadaan edellinen tulos muistista. 
- Jos muistissa oleva sisältö sopii osaksi syötteessä olevaa lauseketta asetetaan se lausekkeen osaksi. Muussa tapauksessa syöte nollataan ja muistin sisältö asetetaan syötteeseen. 

## Esimerkkejä syötteistä
- numerot 
- desimaalierotin ``.``
- peruslaskutoimitukset esim.``1.5/2=0.75``
- potenssi ``2^3=8.0``
- sulut ``1*2+(2-1)=3.0``
- neliöjuuri ``√(4)=2.0``, r-näppäin
- trigonometriset funktiot sini, kosini ja tangentti esim.``sin(3)``, s-,c- ja t-näppäimet
- syötteen poisto kokonaan **AC** ja delete-näppäimellä.
- viimeisen merkin poisto syötteestä **C** ja backspace-näppäimellä.


