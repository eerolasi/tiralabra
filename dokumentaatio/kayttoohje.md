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
![laskinkuva](https://github.com/eerolasi/tiralabra/blob/main/dokumentaatio/laskin.png)

## Syötteet
- Syötteen voi antaa sekä käyttöliittymän nappien kautta että näppäimistöllä.

## Esimerkkejä syötteistä
- numerot
- desimaalierotin ``.``
- yhteenlasku ``1+2=3``
- vähennyslasku ``1-2=-1``
- kertolasku ``1*2=2``
- jakolasku ``1/2=0.5``
- potenssilasku ``2^2=4``
- sulut ``1*2+(2-1)=3``
- sini ``sin(3)``
- kosini ``cos(1+2)``
- syötteen poisto kokonaan **AC**
- viimeisen merkin poisto syöttteestä **C**


