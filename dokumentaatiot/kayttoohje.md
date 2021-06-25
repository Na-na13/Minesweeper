## Käyttöohje

### Asentaminen

Tässä asennusohjeessa oletetaan, että käyttäjällä on käytössä python3, pip3 ja poetry. Jos näitä ei ole asennettuna, pitää ne ensin asentaa, jotta prjoketin saa toimimaan seuraavien ohjeiden mukaisesti.

1. Kloonaa projekti tai lataa projektin zip-tiedosto
2. Asenna poetryn riippuvuudet   
```bash
poetry install
```
4. Suorita ohjelma
```bash
poetry run invoke start
```


### Pelin pelaaminen

Käynnistettäessä peli ensimmäisenä avautuu pelin aloitusikkuna, josta pystyy valitsemaan haluaako pelaaja itse pelata vai katsoa botin pelaamista. Seuraavassa ikkunassa valitaan pelin vaikeustaso kolmesta vaihtoehdosta: Helppo (10x10 pelialue, jossa 10 miinaa), Normaali (16x16 pelialue, jossa 40 miinaa) ja Vaikea (30x16 pelialue, jossa 99 miinaa). Kun vaikeustaso on valittu, avautuu pelinäkymä ja peliä voi alkaa pelata. 

Pelin ideana on saada avattua kaikki miinattomat ruudut siten, ettei kertaakaan avaa ruutua, jossa on miina. Ruudun saa avattua klikkaamalla ruutua hiiren ykköspainikkeella. Avatussa ruudussa oleva numero on vihje kertoo kuinka monta miinaa ruudun avaamattomissa naapuriruuduissa on yhteensä. Miinojen sijainnit voi siten päätellä loogisesti, mutta eteen voi tulla, varsinkin vaikeimalla tasolla, tilanteita, joissa ainut mahdollisuus on vain arvata miinan sijainti. Pelaaja pystyy merkitsemään epäilemänsä miinaruudut klikkaamalla hiiren kakkospainikkeella, jolloin ruutuun ilmestyy *?* -merkki. Epäilymerkinnän saa poistettua klikkaalammal epäilty ruutua uudelleen hiiren kakkospainikkeella. Peli-ikkunan alalaidassa on laskuri, joka laskee pelaajan merkitsemiä miinaepäilyjä. Kun laskuri on nollassa, pitäisi kaikkien jäljellä olevien avaamattomien ruutujen olla miinattomia, jos pelaaja on merkannut miinaepäilyt oikein.

Kun pelaaja on avannut kaikki miinattomat ruudut, piirtyvät miinaruudut pelikentälle vihreinä. Jos pelaaja klikkaa miinaa, miinaruudut piirtyvät punaisina. Tämän jälkeen kerran klikkaamalla pelialuetta avautuu lopetusikkuna, joka kertoo vielä pelin voitosta/häviöstä. Lisäksi tässä ikkunassa pelaaja pystyy haluaako pelata uudelleen, vaihtaa vaikeustasoa tai palata aloitusikkunaan.
