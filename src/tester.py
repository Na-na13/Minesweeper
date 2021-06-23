import minesweeper
import solver_bot

E = (10,10,10)
N = (16,16,40)
H = (30,16,99)

class Tester:

    def __init__(self,level,times):
        """ Testaa botin suoriutumista pelin ratkaisemisessa.

        parametrit:
            level (E,N tai H): testaukseen valittu vaikeustaso
            times (kokonaisluku): testaukseen valittu pelaus kertojen määrä 
        """
        self.level = level
        self.times = times

    def start(self):
        """Suorittaa botin testaamisen ja tulostaa testisilmukan jälkeen tulosraportin.
        """
        i = 0
        wincounter = 0
        losecounter = 0
        while i < self.times:
            game = minesweeper.Minesweeper(self.level[0],self.level[1],self.level[2])
            if game.minemap[0][0] == 10:
                continue
            bot = solver_bot.SolverBot(self.level[0],self.level[1],self.level[2],game)
            gameloop = minesweeper.MSGameLoop(game,self.level[0],self.level[1],bot)
            gameloop.start(self.level[0],self.level[1])
            if gameloop.gamewin == True:
                i += 1
                wincounter += 1
            else:
                i += 1
                losecounter += 1
        print(f"Voitot: {wincounter}")
        print(f"Häviöt: {losecounter}")
        print(f"Voittoprosentti: {(wincounter/self.times)*100} %")

if __name__ == "__main__":
    test = Tester(E,10)
    test.start()
