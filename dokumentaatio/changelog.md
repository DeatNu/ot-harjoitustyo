## Viikko 3

- Lisätty skripti uusille tietokannoille ja käyttäjien lisäykselle
- Lisätty skipti maksujen lisäämiselle ja maksujen hakemiselle tietokannasta
- Lsiätty 3 UI-elementtiä; ikkuna käyttäjien luomiselle, toinen sisäänkirjautumiseen ja kolmas pääohjelman käytölle
- Lisätty pääohjelma, jolla sovellus pyörii
- Lisätty testejä tietokannan perustamiselle ja käyttäjien lisäämiselle

## Viikko 4
- Lisätty nettorahamäärä kummallekin käyttäjälle
- Lisätty erilliset kentät maksuosuuksille
- Lisätty kaksi jakamistyyppiä; 50-50 ja vapaa jakaminen
- Lisätty 50-50 jakamiselle reaaliaikainen täyttö toiseen kenttään
- Lisätty jakamistavan muutos checkboxeilla
- Uudelleennimetty tietokanta
- Uusi teste access.py:lle
- Uusia labeleita

## Viikko 5
- Parannettu checkboxien toimintaa
- Lisätty uusia labeleita
- Korjattu virheviesti maksua lisättäessä
- Käyttäjien nimet näkyvät kenttien yläpuolella
- Lisätty listox, jossa näkyy kaikki maksut
- Listboxiin lisätty scrollbar
- 50-50 jakaminen toimii nyt kumpaankin suuntaan
- Koodi jaettu paremmin funktioiden avulla
- Kansiorakenne muutettu
- Lisää testejä tietokantoihin liittyen
- Suuret summat muutetaan nyt kymmenpotenssimuotoon, jotta ikkunan mittasuhteet eivät hajoa
- Jatkettu koodin kommentointia

## Viikko 6
- Lisätty mahdollisuus tarkistaa sovellukseen lisätyt käyttäjänimet kirjautuessa
- Jaettu ui:hin liittyvät asiat kahteen tiedostoon ja luotu näille oma kansio
- Käyttäjä luo nyt myös salasanan
- Salasana piilotetaan kirjautuessa "*"-merkeillä
- Salasana tiivistetään ("hashed") ennen tietokantaan viemistä saltin kanssa
- Summa värjätty tilanteen mukaan; vihreä; käyttäjä on maksanut enemmän, punainen -> käyttäjä velkaa toiselle, musta -> tasatilanne
- Aloitettu docstringien lisäys

## Viikko 7
- Jaettu ui_main.py:n ominaisuuksia erillisiin tiedostoihin koodin selkeyttämiseksi
- Lisätty docstringejä