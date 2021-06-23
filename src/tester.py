import minesweeper
import solver_bot

E = (10,10,10)
N = (16,16,40)
H = (30,16,99)

class Tester:

    def __init__(self):
        self.test = True

    def start(self):
        i = 0
        wincounter = 0
        losecounter = 0
        guesses = 0
        while i < 200:
            game = minesweeper.Minesweeper(H[0],H[1],H[2])
            if game.minemap[0][0] == 10:
                continue
            bot = solver_bot.SolverBot(H[0],H[1],H[2],game)
            gameloop = minesweeper.MSGameLoop(game,H[0],H[1],bot)
            gameloop.start(H[0],H[1])
            if gameloop.gamewin == True:
                #print("Voitto!")
                i += 1
                wincounter += 1
            else:
                i += 1
                losecounter += 1
            #print("Täällä")
            guesses += bot.guesses
        print(f"Voitot: {wincounter}")
        print(f"Häviöt: {losecounter}")
        print(f"Voittoprosentti: {(wincounter/200)*100} %")
        print(f"Arvauksia keskimäärin/peli: {guesses/200:.2f}")

if __name__ == "__main__":
    test = Tester()
    test.start()
