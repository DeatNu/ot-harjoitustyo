# Käyttöohje

Riippuvuuksien asentamisen jälkeen sovellus käynnistetään komennolla _poetry run invoke start_.
&nbsp; <br>
&nbsp; <br>
Tämän jälkeen kumpikin käyttäjä luo itselleen __\*uniikin\*__ käyttäjätunnuksen ja salasanan. "__Enter__"-napista pääsee eteenpäin, kun käyttäjä ja salasana ovat uniikkeja ja pituudeltaan vähintään yksi merkki. 
&nbsp; <br>
&nbsp; <br>
Käyttäjien luomisen jälkeen pääsee sisäänkirjautumisnäkymään, johon samaan tapaan kirjoitetaan käyttäjätunnus ja salasana. Jos käyttäjä ei muista tunnustaan, "__Forgot Username?__" -valinnalla sen saa esiin.
&nbsp; <br>
&nbsp; <br>
Pääikkunassa käyttäjä näkee vasemmalla suhteellisen velan (__Total__). Vihreällä värillä oleva positiivinen luku tarkoittavat, että käyttäjä on maksanut toista käyttäjää enemmän. Punainen ja negatiivinen luku puolestaan tarkoittavat, että käyttäjä on toiselle velkaa kyseisen summan.
&nbsp; <br>
&nbsp; <br>
Käyttäjä voi lisätä maksun kahdella tavalla; hän voi valita tavan __50-50-splitting__, jolloin jompaankumpaan laatikkoon kirjoitettu summa kopioituu toiseen laatikkoon. Vaihtoehtoisesti käyttäjä voi valita __Choose shares__ -tavan, jolloin luvut voivat olla toisistaan eroavat. Laatikoihin voi kirjoittaa vain epänegatiivisia lukuja.
&nbsp; <br>
&nbsp; <br>
Käyttäjä voi myös halutessaan lisätä kommentin, joka liitetään maksun yhteyteen. Maksun lisääjä, hänen osuutensa, toisen osuus sekä mahdollinen kommentti tulevat maksun lisäämisen jälkeen näkyville ruudulla näkyvään kenttään. Maksu lisätään __Enter__-napilla, kun kummassakin kentässä on sallittu summa.
&nbsp; <br>
![main window](main_window1.png)
&nbsp; <br>
## Ongelmatilanteet
&nbsp; <br>
Jos käyttäjä unohtaa salasanansa, syöttää väärät maksutiedot (tai haluaa nollata tilanteen) tai jotain odottamatonta tapahtuu, täytyy ohjelma resetoida. Tämä käy helpoiten komennolla _poetry run invoke test_, joka suorittaa testit ja samalla poistaa tietokannan. __Tietokannan poisto on peruuttamaton toimenpide, eikä tietoja saa palautettua__. 
