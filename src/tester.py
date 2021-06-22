from collections import deque
#import ui
import minesweeper
import solver_bot
import pygame

class Tester:

    def __init__(self):
        self.gamecounter = 0
        self.wincounter = 0
        self.losecounter = 0
        self.guesscounter = 0
        #self.eventqueue = deque()
        #self.first_move = False
    
#    def next_move(self):
#        if self.first_move == False:
#            self.start()
#            return [self.eventqueue.popleft(),self.eventqueue.popleft()]

#    def start(self):
#        self.eventqueue.append(Event(pygame.MOUSEBUTTONDOWN, (115,140),1))
#        self.eventqueue.append(Event(pygame.MOUSEBUTTONDOWN, (115,140),1))
#        self.first_move = True
    def start(self):
        i = 0
        wincounter = 0
        losecounter = 0
        while i < 100:
            game = minesweeper.Minesweeper(16,16,40)
            if game.minemap[0][0] == 10:
                continue
            bot = solver_bot.SolverBot(16,16,40,game) # tämä on bottia varten
            gameloop = minesweeper.MSGameLoop(game,16,16,bot) # tämä on bottia varten
            gameloop.start(16,16)
            if gameloop.gamewin == True:
                print("Voitto!")
                i += 1
                wincounter += 1
            else:
                i += 1
                losecounter += 1
            print("Täällä")
        print(f"Voitot: {wincounter}")
        print(f"Häviöt: {losecounter}")
        print(f"Voittoprosentti: {(wincounter/100)*100} %")

if __name__ == "__main__":
    test = Tester()
    test.start()

class Event:

    def __init__(self,type,pos,but):
        self.type = type
        self.pos = pos
        self.button = but