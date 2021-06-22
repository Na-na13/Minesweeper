#Solver_bot
from collections import deque
import pygame
import ui
import minesweeper
from random import choice


class SolverBot:
    
    def __init__(self,w,h,mines,game):
        self.game = game
        self.gamegrid = [[20 for a in range(w)] for b in range(h)]
        self.w = w
        self.h = h
        self.eventqueue = deque()
        self.first_move = True
        self.sidecells = []
        self.add_sidecells()
        
    def add_sidecells(self):
        for x in range(0,self.w):
            if (x,0) not in self.sidecells:
                self.sidecells.append((x,0))
            if (x,self.h-1) not in self.sidecells:
                self.sidecells.append((x,self.h-1)) 
        for y in range(0,self.h):
            if (0,y) not in self.sidecells:
                self.sidecells.append((0,y))
            if (self.w-1,y) not in self.sidecells:
                self.sidecells.append((self.w-1,y))
        self.sidecells.pop(0)

    def next_move(self):
        if self.first_move:
            self.eventqueue.append(Event(pygame.MOUSEBUTTONDOWN, (10,10),1))
            self.first_move = False
        if len(self.eventqueue) > 0:
            return [self.eventqueue.popleft()]
        else:
            self.run_solver()
            if len(self.eventqueue) > 0:
                return [self.eventqueue.popleft()]
            else:
                self.open_random()
                if len(self.eventqueue) > 0:
                    return [self.eventqueue.popleft()]
                else:
                    self.open_random()
                    return [self.eventqueue.popleft()]

    def run_solver(self):
            mines = self.search_mines()
            for mine in mines:
                x = mine[1]
                y = mine[0]
                if mine in self.sidecells:
                    self.sidecells.remove(mine)
                self.eventqueue.append(Event(pygame.MOUSEBUTTONDOWN,((x*20)+(x*5)+15, (y*20)+(y*5)+15),3))
            frees = self.search_frees()
            for free in frees:
                xx = free[1]
                yy = free[0]
                if self.gamegrid[yy][xx] == 20:
                    if free in self.sidecells:
                        self.sidecells.remove(free)
                    self.eventqueue.append(Event(pygame.MOUSEBUTTONDOWN,((xx*20)+(xx*5)+15, (yy*20)+(yy*5)+15),1))
    
    def find_buffercells(self):
        buffercells = []
        for y in range(self.h):
            for x in range(self.w):
                if 1 <= self.gamegrid[y][x] <= 8:
                    buffercells.append((x,y))
        return buffercells

    def search_mines(self):
        buffer = self.find_buffercells()
        mine_pos = []
        for cell in buffer: # i = x, j = y
            mine_counter = 0
            pos = []
            i = cell[0]
            j = cell[1]
            if j-1 >= 0 and i-1 >= 0:
                if self.gamegrid[j-1][i-1] == 20: # viistoon vasemmalle ylös
                    pos.append((j-1,i-1))
                if self.gamegrid[j-1][i-1] == 30:
                    mine_counter += 1
            if j-1 >= 0:
                if self.gamegrid[j-1][i] == 20: # suoraan ylös
                    pos.append((j-1,i))
                if self.gamegrid[j-1][i] == 30:
                    mine_counter += 1
            if j-1 >= 0 and i+1 < self.w:
                if self.gamegrid[j-1][i+1] == 20: # viistoon oikealle ylös
                    pos.append((j-1,i+1))
                if self.gamegrid[j-1][i+1] == 30:
                    mine_counter += 1
            if i-1 >= 0:
                if self.gamegrid[j][i-1] == 20: # vasen
                    pos.append((j,i-1))
                if self.gamegrid[j][i-1] == 30:
                    mine_counter += 1
            if i+1 < self.w:
                if self.gamegrid[j][i+1] == 20: # oikea
                    pos.append((j,i+1))
                if self.gamegrid[j][i+1] == 30:
                    mine_counter += 1
            if j+1 < self.h and i-1 >= 0:
                if self.gamegrid[j+1][i-1] == 20: # viistoon vasemmalle alas
                    pos.append((j+1,i-1))
                if self.gamegrid[j+1][i-1] == 30:
                    mine_counter += 1
            if j+1 < self.h:
                if self.gamegrid[j+1][i] == 20: # suoraan alas
                    pos.append((j+1,i))
                if self.gamegrid[j+1][i] == 30:
                    mine_counter += 1
            if j+1 < self.h and i+1 < self.w:
                if self.gamegrid[j+1][i+1] == 20: # viistoon oikealle alas
                    pos.append((j+1,i+1))
                if self.gamegrid[j+1][i+1] == 30:
                    mine_counter += 1
            if self.gamegrid[j][i] - mine_counter == 0:
                continue
            if self.gamegrid[j][i] - mine_counter == len(pos):
                for cords in pos:
                    if cords not in mine_pos:
                        mine_pos.append(cords)
        for mine in mine_pos:
            self.gamegrid[mine[0]][mine[1]] = 30
        return mine_pos
    
    def search_frees(self):
        buffer2 = self.find_buffercells()
        free_pos = []
        for cell2 in buffer2: # i = x, j = y
            counter = 0
            pos = []
            ii = cell2[0]
            jj = cell2[1]
            if jj-1 >= 0 and ii-1 >= 0:
                if self.gamegrid[jj-1][ii-1] == 30: # viistoon vasemmalle ylös
                    counter += 1
                if self.gamegrid[jj-1][ii-1] == 20:
                    pos.append((jj-1,ii-1))
            if jj-1 >= 0:
                if self.gamegrid[jj-1][ii] == 30: # suoraan ylös
                    counter += 1
                if self.gamegrid[jj-1][ii] == 20:
                    pos.append((jj-1,ii))
            if jj-1 >= 0 and ii+1 < self.w:
                if self.gamegrid[jj-1][ii+1] == 30: # viistoon oikealle ylös
                    counter += 1
                if self.gamegrid[jj-1][ii+1] == 20:
                    pos.append((jj-1,ii+1))
            if ii-1 >= 0:
                if self.gamegrid[jj][ii-1] == 30: # vasen
                    counter += 1
                if self.gamegrid[jj][ii-1] == 20:
                    pos.append((jj,ii-1))
            if ii+1 < self.w:
                if self.gamegrid[jj][ii+1] == 30: # oikea
                    counter += 1
                if self.gamegrid[jj][ii+1] == 20:
                    pos.append((jj,ii+1))
            if jj+1 < self.h and ii-1 >= 0:
                if self.gamegrid[jj+1][ii-1] == 30: # viistoon vasemmalle alas
                    counter += 1
                if self.gamegrid[jj+1][ii-1] == 20:
                    pos.append((jj+1,ii-1))
            if jj+1 < self.h:
                if self.gamegrid[jj+1][ii] == 30: # suoraan alas
                    counter += 1
                if self.gamegrid[jj+1][ii] == 20:
                    pos.append((jj+1,ii))
            if jj+1 < self.h and ii+1 < self.w:
                if self.gamegrid[jj+1][ii+1] == 30: # viistoon oikealle alas
                    counter += 1
                if self.gamegrid[jj+1][ii+1] == 20:
                    pos.append((jj+1,ii+1))
            if self.gamegrid[jj][ii] == counter:
                for cords in pos:
                    if cords not in free_pos:
                        free_pos.append(cords)
        return free_pos

    def open_random(self):
        if len(self.sidecells) > 0:
            valid = False
            while not valid:
                if len(self.sidecells) == 0:
                    break
                random = choice(self.sidecells)
                x = random[0]
                y = random[1]
                if self.gamegrid[y][x] == 20:
                    self.eventqueue.append(Event(pygame.MOUSEBUTTONDOWN,((x*20)+(x*5)+15, (y*20)+(y*5)+15),1))
                    self.sidecells.remove(random)
                    valid = True
                else:
                    self.sidecells.remove(random)
        else:
            valid = False
            while not valid:
                cells = self.find_buffercells()
                random = choice(cells)
                pos = []
                x = random[0]
                y = random[1]
                if y-1 >= 0 and x-1 >= 0:
                    if self.gamegrid[y-1][x-1] == 20: # viistoon vasemmalle ylös
                        pos.append((y-1,x-1))
                if y-1 >= 0:
                    if self.gamegrid[y-1][x] == 20: # suoraan ylös
                        pos.append((y-1,x))
                if y-1 >= 0 and x+1 < self.w:
                    if self.gamegrid[y-1][x+1] == 20: # viistoon oikealle ylös
                        pos.append((y-1,x+1))
                if x-1 >= 0:
                    if self.gamegrid[y][x-1] == 20: # vasen
                        pos.append((y,x-1))
                if x+1 < self.w:
                    if self.gamegrid[y][x+1] == 20: # oikea
                        pos.append((y,x+1))
                if y+1 < self.h and x-1 >= 0:
                    if self.gamegrid[y+1][x-1] == 20: # viistoon vasemmalle alas
                        pos.append((y+1,x-1))
                if y+1 < self.h:
                    if self.gamegrid[y+1][x] == 20: # suoraan alas
                        pos.append((y+1,x))
                if y+1 < self.h and x+1 < self.w:
                    if self.gamegrid[y+1][x+1] == 20: # viistoon oikealle alas
                        pos.append((y+1,x+1))
                
                if len(pos) > 0:
                    valid = True
            result = choice(pos)
            xx = result[1]
            yy = result[0]
            self.eventqueue.append(Event(pygame.MOUSEBUTTONDOWN,((xx*20)+(xx*5)+15, (yy*20)+(yy*5)+15),1))

class Event:

    def __init__(self,type,pos,but):
        self.type = type
        self.pos = pos
        self.button = but

