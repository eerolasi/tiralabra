# Testausdokumentti

## Testauskattavuus
![testausdokumentti](https://github.com/eerolasi/tiralabra/blob/main/dokumentaatio/testauskattavuus.png)


## Testattu
Sovelluslogiikka on testattu automaattisella yksikkötestauksella. Järjestelmätestausta on suoritettu manuaalisesti erilaisin syöttein ja tuloksia vertaillen toiseen laskimeen.

## Testien suorittaminen
GitHub Actions suorittaa testit aina GitHubiin uuden koodin pushauksen yhteydessä.


### Käynnistä virtuaaliympäristö juurihakemistossa
```
poetry shell
```

### Asenna riippuvuudet
```
poetry install 
```

### Suorita testit
```
poetry run invoke test
```

### Testauskattavuusraportti

```
poetry run invoke coverage
```

