## Testausdokumentti

Loin ratkaisijabottia varten oman testusluokan, jolla pystyy testaamaan botin suoriutumista pelien ratkaisemisessa. Testattaessa pystyy valitsemaan, mitä vaikeustasoa haluaa testata ja kuinka monta kertaa botti pelaa peliä. Testaus on toteutettu siten, että aloitusruutu on aina sama, vasen yläkulma, ja jos pelikentän generoimisen jälkeen huomataan, että aloitusruudussa on miina, generoidaan pelikenttä uudelleen. Uudelleen generointi tehdään siksi, koska aloituruudun miinallisuus ei kerro botin suoriutumisesta mitään ja siten vääristäisi tuloksia.

Testattaessa pelin koodiin pitää tehdä pieniä muutoksia, jotta botti pystyy pelaamaan pelit ilman ihmisen avustamista. Pelisilmukasta täytyy vaihtaa rivi 146 toimivaksi ja piilottaa 147 sekä vaihtaa rivi 206 toimivaksi ja piilottaa rivit 206 ja 207:  
```python
...
145 else:   
146     next_move = [solver_bot.Event(pygame.MOUSEBUTTONDOWN, (115,140),1)] # Testauksen rivi 
147     #next_move = []
...
```

```python
...
204 else:
205     return #Testauksen rivi
206     #play_time = f"{self.end_time - self.start_time:.2f}"
207    #EndWindow(w,h,self.game.mines,play_time,self.gamewin,self.solver)
...
```

Koodin muutoksen jälkeen testiluokan pystyy suorittamaan seuraavasti:
```bash
poetry run invoke test
```
Testauksen pystyy käynnistämään myös suorittamalla tiedoston *tester.py*.

Testasin botin suoritumista pelattamalla sillä 500 peliä jokaisella vaikeustasolla. Alla olevaan taulukkoon olen listannut tulokset. Tulosten tarkkuuteen vaikuttaa jonkin verran satunnaisuus, sillä pelikentän miinapaikat valitaan satunnaisesti ja peleissä tulee vastaan tilanteita, joissa pääse etenemään vain valitsemalla seuraavaksi avattavaksi ruuduksi satunnaisen ruudun.

Vaikeustaso | Voitot | Häviöt | Voitto%
----------- | ------ | ------ | -------
Helppo|434|66|86,8 %
Normaali|229|271|45,8 %
Vaikea|8|492|1,6 %
