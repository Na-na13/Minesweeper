from minesweeper import Minesweeper, MSGameLoop
from solver_bot import SolverBot

E = (10,10,10)
N = (16,16,40)
H = (30,16,99)

class Tester:

    def __init__(self,level,times):
        """ Testaa botin suoriutumista pelin ratkaisemisessa.

        parametrit:
            level: testaukseen valittu vaikeustaso (E = Easy, N = Normal, H = Hard)
            times: testaukseen valittu pelaus kertojen määrä
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
            game = Minesweeper(self.level[0],self.level[1],self.level[2])
            if game.minemap[0][0] == 10:
                continue
            bot = SolverBot(self.level[0],self.level[1],game)
            gameloop = MSGameLoop(game,self.level[0],self.level[1],bot)
            gameloop.start(self.level[0],self.level[1])
            if gameloop.gamewin:
                i += 1
                wincounter += 1
            else:
                i += 1
                losecounter += 1
            print("Games played:", i)
        print("Result report")
        print(f"Wins: {wincounter}")
        print(f"Loses: {losecounter}")
        print(f"Win%: {(wincounter/self.times)*100} %")

if __name__ == "__main__":
    try:
        level = input("Choose level (E, N, H): ")
        times = int(input("Choose how many times: "))
    except ValueError:
        level = "X"
        times = -1

    if level in ["E", "N", "H"] and times > 0:
        if level == "E":
            test = Tester(E,times)
            test.start()
        if level == "N":
            test = Tester(N,times)
            test.start()
        if level == "H":
            test = Tester(H,times)
            test.start()
    else:
        print("Invalid input")
