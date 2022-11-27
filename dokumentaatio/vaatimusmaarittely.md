# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksella voi pitää kirjaa käyttäjien menoista. Sovellukseen ilmoitetaan maksuja, jotka jaetaan käyttäjien kesken, jolloin käyttäjät näkevät velkansa toisille.

## Toiminnallisuudet ja rakenne

### Käyttöliittymä
- Kirjautumisikkuna, jossa voi valita käyttäjän (tehty)
- Pääikkuna, jossa näkee rahamäärän, jonka toinen on velkaa sinulle tai sinä hänelle (tehty)
- Vihreä väri: käyttäjällä on saatavia, punainen väri: käyttäjä velkaa toiselle
- Pääikkunassa myös maksunlisäys, jossa voi ilmoittaa summan ja kommentin maksuun liittyen (1/2 tehty)

### Sovelluslogiikka
- Pääsy tietokantoihin
- Salasana ja sen varmistaminen

### Tietokannat
- Ainakin yksi SQL-taulu, jossa maksajan nimi, rahamäärä, kommentti (esim. "sähkölasku", "ravintolareissu") (melkein tehty)

## Jatkokehitysideoita
- Rahamäärän jako manuaalisesti (esim. 70-30 eikä aina vain puoliksi) (tehty)
- Usemman käyttäjän muodostama ryhmä, jäsenten lisäys jälkikäteen
- Profiilin personointi (esim. profiilikuva)
- Asetukset (esim. nimen muokkaus, jäsenen tai ryhmän poisto, saldon nollaus)
- Lista maksuista (osuudet ja kommentti)