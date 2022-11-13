# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksella voi pitää kirjaa käyttäjien menoista. Sovellukseen ilmoitetaan maksuja, jotka jaetaan käyttäjien kesken, jolloin käyttäjät näkevät velkansa toisille.

## Toiminnallisuudet ja rakenne

### Käyttöliittymä
- Kirjautumisikkuna, jossa voi valita käyttäjän
- Pääikkuna, jossa näkee rahamäärän, jonka toinen on velkaa sinulle tai sinä hänelle
- Pääikkunassa myös maksunlisäys, jossa voi ilmoittaa summan ja kommentin maksuun liittyen

### Sovelluslogiikka
- Luokat käyttäjille, maksuille
- Pääsy tietokantoihin

### Tietokannat
- Ainakin yksi SQL-taulu, jossa maksajan nimi, rahamäärä, kommentti (esim. "sähkölasku", "ravintolareissu")

## Jatkokehitysideoita
- Rahamäärän jako manuaalisesti (esim. 70-30 eikä aina vain puoliksi)
- Usemman käyttäjän muodostama ryhmä, jäsenten lisäys jälkikäteen
- Profiilin personointi (esim. profiilikuva)
- Asetukset (esim. nimen muokkaus, jäsenen tai ryhmän poisto, saldon nollaus)