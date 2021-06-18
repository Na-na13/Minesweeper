# Miinaharavan ratkaisija

#### ohjelmointikieli: python
#### opinto-ohjelma: tietojenkäsittelytieteen kandidaatti
#### dokumentaation kieli: suomi


Miinaharava on yksinpelattava ongelmanratkaisupeli, jossa *n* x *m* -peliruudukosta pyritään avaamaan kaikki ruudut, joissa ei ole miinaa. Pelin ratkaisemiseksi on kehitelty eri tyylisiä algoritmeja. Eräs tapa, jota hyödynnetään tässä Miinaharavan ratkaisijassa, on ajatella Miinaharava-peliä rajoitelaskennan ongelmana. Pyrkimyksenä on siis määritellä jokaiselle avaamattomalle pelikentän ruudulle arvo siten, ettei yhtäkään viereisistä miinoista kertovien vihjeiden asettamaa rajoitusta rikota.

### Algoritmin toiminta

Miinaharavan peli etenee siten, että pelaaja avaa peliruudukon ruutuja. Jokaisella ruudulla, jossa ei ole miinaa, on kokonaislukuarvo 0,..,8, joka ilmaisee ruudun vierekkäisten miinojen määrän. Toisin sanoen, jos ruudulla on arvo *n*, sillä on *n* vierekkäistä miinaa eli ruutua, jota ei tule aukaista pelin voittamiseksi. Ruudun, jonka arvo on 0, vieressä ei ole yhtään miinaa ja vastaavasti ruudun, jonka arvo on 8, kaikki vierekkäiset ruudut ovat miinoja. Kokonaislukuarvojen perusteella pelaaja voi loogisesti päätellä miinojen sijainteja peliruudukossa ja merkata ruutuja mahdollisiksi miinoiksi. Kuitenkaan kaikkien miinojen tarkkoja sijainteja ei voi välttämättä päätellä niihin viittaavien lukuarvojen perusteella. Eteen voi tulla tilanne, joka vaatii pelaajalta silkkaa arvaamasta. Tämänkaltaiset tilanteet aiheuttavat haasteita pelin ratkaisualgoritmien suunnittelussa. 

Ajateltaessa Miinaharavaa rajoitelaskennan ongelmana jokaisella ruudulla on arvo 1 tai 0 eli ruudussa on miina (1) tai ruutu on miinaton (0). Kun pelaaja avaa ruudun *x*, se asettaa rajoituksia sen naapuriruuduille sieltä avautuvat kokonaislukuarvon perusteella. Tämän perusteella voidaan tehdä päätelmiä peliruudukon miina-asetelmista. Triviaalit rajoitteet ovat sellaisia, joiden avulla pystytään varmasti sanomaan, että joko kaikki ruudun *x* avaamattomat naapuriruudut ovat miinoja tai miinattomia. Ratkaisijan ideana on käsitellä nämä triviaalit rajoitteet ensin, jotta saadaan pelikenttää mahdollisimman paljon auki. Kun pelikentällä ei enää ole avaamattomia ruutuja, joiden miinallisuutta triviaalit rajoiteet ilmaisisivat, siirrytään suorittamaan peruuttavaa hakua, jonka avulla saadaan selville kaikki mahdolliset tavat miinojen sijainnille sen hetkisessä pelitilanteessa. Näin pystytään laskemaan todennäköisyyksiä miinojen sijainneille. Jos tälläkään periaatteella ei saada kuin 50% todennäköisyys miinalle kaikkin ruutuihin, pitää avata satunnainen ruutu.

### Tietorakenteet
Miinaharava-peliä on loogista ajatella kaksiulotteisena taulukkona.

### Ohjelman syötteet
Pelin alussa pelaaja valitsee vaikeustason kolmesta vaihtoehdosta. Vaikeustaso määrittelee pelikentän koko sekä miinojen määrä noudattaa Windowsin Miinaharava-pelin vastaavia. Näiden parametrien avulla algoritmi pystyy käsittelemään kaksiuloitteisena taulukkona esitettyä pelikenttää.    

Miinaharava-pelin pelaamisessa pelaaja käsittelee pelikentän ruutuja hiiren klikkauksilla. Hiiren painikkeella 1 avataan avaamaton pelikentän ruutu ja painikkeella 3 merkataan jokin avaamaton ruutu mahdolliseski miinaksi. Ratkaisija vastaavasti simuloi näitä ihmispelaajan tekemiä hiiren liikkeitä.    

### Aika- ja tilavaativuus
Käsiteltävät syötteet ovat sen verran pieniä, että algoritmin ei käytännössä tarvitse olla kovin tehokas pystyäkseen käsittelemään syötteitä tarpeeksi nopeasti. Kaksiulotteisen taulukon läpikäynnissä tulen käyttämään sisäkkäisiä silmukoita, joten aikavaativuus tulee olemaan jotakuinkin *O(wh)*, missä *w* on pelikentän leveys ja *h* pelikentän korkeus.

Algoritmin toteutuksessa tulen tarvitsemaan useampaa samankokoista kaksiulotteista taulukkoa pitämään kirjaa pelin eri osa-alueista, kuten pelikentän miinojen sijainnesta sekä pelikentän avatuista/avaamattomista ruuduista.

### Lähteet
Miinaharavan ratkaisijan suunnittelussa on käyttänyt apuna David Becerran tutkielmaa [*Algorithmic Approaches to Playing Minesweeper*]( https://dash.harvard.edu/bitstream/handle/1/14398552/BECERRA-SENIORTHESIS-2015.pdf?sequence=1&isAllowed=y)
