#Solver_bot
from collections import deque
import pygame
import ui
import minesweeper

class SolverBot:
    
    def __init__(self,w,h,mines,game):
        self.game = game
        self.gamegrid = [[20 for a in range(w)] for b in range(h)]
        self.w = w
        self.h = h

    def run_solver(self):
        self.counter = 0
        eventlist = []
        event = Event(pygame.MOUSEBUTTONDOWN, (10,10),1)
        eventlist.append(event)
        while True:
            self.counter += 1
            if self.counter < 3:
                continue
            self.counter = 0
            mines = self.find_buffercells()
            for mine in mines:
                x = mine[0]
                y = mine[1]
                eventlist.append(Event(pygame.MOUSEBUTTONDOWN,((y*20)+(y*5)-10, (x*20)+(x*5)-10),3))
            e = eventlist.pop(0)
            print(e.pos)
            return [e]
    
    def find_buffercells(self):
        buffer = []
        for y in range(self.h):
            for x in range(self.w):
                if 1 <= self.gamegrid[y][x] <= 8:
                    buffer.append((y,x))
        print(buffer)
        return self.search_mines(buffer)
    
    def search_mines(self,buffer):
        mine_pos = []
        counter = 0
        for cell in buffer: # i = x, j = y
            pos = []
            i = cell[1]
            j = cell[0]
            if j-1 >= 0 and i-1 >= 0:
                if self.gamegrid[j-1][i-1] == 20: # viistoon vasemmalle ylös
                    counter += 1
                    pos.append((j-1,i-1))
            if j-1 >= 0:
                if self.gamegrid[j-1][i] == 20: # suoraan ylös
                    counter += 1 
                    pos.append((j-1,i))
            if j-1 >= 0 and i+1 < self.w:
                if self.gamegrid[j-1][i+1] == 20: # viistoon oikealle ylös
                    counter += 1
                    pos.append((j-1,i+1))
            if i-1 >= 0:
                if self.gamegrid[j][i-1] == 20: # vasen
                    counter += 1
                    pos.append((j,i-1))
            if i+1 < self.w:
                if self.gamegrid[j][i+1] == 20: # oikea
                    counter += 1
                    pos.append((j,i+1))
            if j+1 < self.h and i-1 >= 0:
                if self.gamegrid[j+1][i-1] == 20: # viistoon vasemmalle alas
                    counter += 1
                    pos.append((j+1,i-1))
            if j+1 < self.h:
                if self.gamegrid[j+1][i] == 20: # suoraan alas
                    counter += 1
                    pos.append((j+1,i))
            if j+1 < self.h and i+1 < self.w:
                if self.gamegrid[j+1][i+1] == 20: # viistoon oikealle alas
                    counter += 1
                    pos.append((j+1,i+1))
            if self.gamegrid[j][i] == len(pos):
                for cords in pos:
                    if cords not in mine_pos:
                        mine_pos.append(cords)
                        #self.gamegrid[cords[0]][cords[1]] = 30
        print(mine_pos)
        return mine_pos


class Event:

    def __init__(self,type,pos,but):
        self.type = type
        self.pos = pos
        self.button = but

