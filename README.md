# Ohjelmistotekniikka

Tässä repositoriossa on velanhallintatyökalun lähdekoodi. Tällä sovelluksella (Pyshare) voi pitää kirjaa velasta esim. kaverin tai kumppanin kanssa. Sovellukseen voi lisätä kummankin osapuolen osuuden maksusta, nähdä oman velkatilanteen, sekä selata maksuja. Käyttäjää voi vaihtaa avaamalla sovelluksen uudelleen. Sovelluksen resetointi onnistuu vaikkapa "poetry run invoke test" -komennon avulla.

#### Dokumentaatio
- [vaatimusmaarittely.md](https://github.com/DeatNu/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [tyoaikakirjanpito.md](https://github.com/DeatNu/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [changelog.md](https://github.com/DeatNu/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [arkkitehtuuri.md](https://github.com/DeatNu/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

#### Käyttö
Ladattuasi ohjelman suorita komento _poetry install_. Tämän jälkeen voit käyttää seuraavia komentoja

_poetry run invoke start_ &rarr; käynnistää ohjelman
<br>
_poetry run invoke test_ &rarr; suorittaa testit
<br>
_poetry run invoke coverage_ &rarr; branch-kattavuus
<br>
_poetry run invoke coverage_report_ &rarr; kattavuusraportti
<br>
_poetry run invoke open_in_browser_ &rarr; kattavuusraportti selaimessa (Firefox)
<br>
_poetry run invoke format_ &rarr; formatointi
<br>
_poetry run invoke lint_ &rarr; linttaus

#### Release:
[Project release](https://github.com/DeatNu/ot-harjoitustyo/releases/tag/viikko5)
