#Solver_bot
from collections import deque
import pygame
import ui
import minesweeper
from random import choice
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

class SolverBot:
    
    def __init__(self,w,h,mines,game):
        self.game = game
        self.gamegrid = [[20 for a in range(w)] for b in range(h)]
        self.w = w
        self.h = h
        self.eventqueue = deque()
        self.first_move = True
        self.sidecells_opened = False

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
            return []
            #else:
            #open random cell

    def run_solver(self):
            mines = self.search_mines()
            #print(mines)
            for mine in mines:
                x = mine[0]
                y = mine[1]
                self.eventqueue.append(Event(pygame.MOUSEBUTTONDOWN,((y*20)+(y*5)+15, (x*20)+(x*5)+15),3))
            frees = self.search_frees()
            #print(frees)
            for free in frees:
                xx = free[0]
                yy = free[1]
                if self.gamegrid[xx][yy] == 20:
                    self.eventqueue.append(Event(pygame.MOUSEBUTTONDOWN,((yy*20)+(yy*5)+15, (xx*20)+(xx*5)+15),1))
    
    def find_buffercells(self):
        buffercells = []
        for y in range(self.h):
            for x in range(self.w):
                if 1 <= self.gamegrid[y][x] <= 8:
                    buffercells.append((y,x))
        return buffercells
    
    def search_mines(self):
        buffer = self.find_buffercells()
        mine_pos = []
        for cell in buffer: # i = x, j = y
            mine_counter = 0
            pos = []
            i = cell[1]
            j = cell[0]
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
        #print(mine_pos)
        return mine_pos
    
    def search_frees(self):
        buffer2 = self.find_buffercells()
        free_pos = []
        for cell2 in buffer2: # i = x, j = y
            counter = 0
            pos = []
            ii = cell2[1]
            jj = cell2[0]
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
        corners = [(self.h-1,0),(self.h-1,self.w-1),(0,self.w-1)]
        random = choice(corners)
        #if self.gamegrid[random[0]][random[1]] == 20:
        #    self.eventqueue.append(Event(pygame.MOUSEBUTTONDOWN,((y*20)+(y*5)+15, (x*20)+(x*5)+15),3))




class Event:

    def __init__(self,type,pos,but):
        self.type = type
        self.pos = pos
        self.button = but

