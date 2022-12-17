# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksella voi pitää kirjaa käyttäjien keskeisistä menoista. Sovellukseen ilmoitetaan maksuja, jotka jaetaan käyttäjien kesken, jolloin käyttäjät näkevät velkansa toisille.

## Toiminnallisuudet ja rakenne

### Käyttöliittymä
- Ikkuna käyttäjien luomiselle ensimmäisellä käyttökerralla (tehty)
- Kirjautumisikkuna, jossa voi kirjautua käyttjätunnuksella ja salasanalla (tehty)
- Pääikkuna, jossa näkee rahamäärän, jonka toinen on velkaa sinulle tai sinä hänelle (tehty)
- Vihreä väri: käyttäjällä on saatavia, punainen väri: käyttäjä velkaa toiselle (tehty)
- Pääikkunassa myös maksunlisäys, jossa voi ilmoittaa summan ja kommentin maksuun liittyen (tehty)
- Lista maksuista (osuudet ja kommentti) (tehty)
- Automaattinen 50-50 jako (tehty)
- Rahamäärän jako manuaalisesti (esim. 70-30 eikä aina vain puoliksi) (tehty)

### Sovelluslogiikka
- Pääsy tietokantoihin (tehty)
- Vaihto ikkunasta toiseen (tehty)
- Salasana ja sen varmistaminen (tehty)

### Tietokannat
- SQL-tietokanta, jossa kaksi taulua
- Taulu käyttäjien tiedoille
- Taulu maksuille (maksaja, osuudet, kommentti) 

## Jatkokehitysideoita
- Usemman käyttäjän muodostama ryhmä, jäsenten lisäys jälkikäteen
- Profiilin personointi (esim. profiilikuva)
- Asetukset (esim. nimen muokkaus, jäsenen tai ryhmän poisto, saldon nollaus)
