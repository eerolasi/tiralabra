# Määrittelydokumentti

**Ohjelmointikieli**: Python  
**Muut hallitut kielet:** JavaScript  
**Dokumentaation kieli:** suomi
**Opinto-ohjelma:** TKT

**Algoritmit ja tietorakenteet:** Shunting Yard-algoritmi ja pino

**Ratkaistava ongelma:** Tieteellinen laskin, jolla voidaan ratkaista matemaattisen lausekkeen arvo.

**Algoritmien ja tietorakenteiden valinta:** Shunting Yard-algoritmillä voidaan muuntaa infix-notaatiolla määritelty matemaattinen lauseke postfix-notaatioksi eli päinvastaiseksi puolalaiseksi notaatioksi (RPN). Infix-notaatiossa operaattorit sijoitetaan operandien väliin kun taas RPN:ässä operaattorit sijoitetaan suoraan operandien jälkeen. RPN sopii hyvin laskimeen, sillä se tekee lausekkeiden arvioinnista yksinkertaisempaa ja helpompaa pinon avulla, jolloin esimerkiksi sulkeita tai prioriteetteja ei tarvitse tarkastella.

**Syötteet:** Syötteenä on käyttäjän antama matemaattinen lauseke, jonka arvo lasketaan. Syöte voi sisältää kokonaislukuja, desimaalilukuja, muuttujia, peruslaskutoimituksia ja funktioita.

**Aika- ja tilavaativuus:** O(n)

**Lähde:** https://en.wikipedia.org/wiki/Shunting_yard_algorithm
