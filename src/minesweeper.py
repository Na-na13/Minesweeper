# Minesweeper
import pygame
from random import randint

class Minesweeper:

    def __init__(self):

        pygame.init()

        self.win_height = 275
        self.win_width = 255
        self.margin = 5
        self.height = 20
        self.width = 20

        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        self.window.fill((0,0,0))
        pygame.display.set_caption("Minesweeper")

        self.draw_grid()
        self.place_mines()
        self.open()
        self.loop()


    def draw_grid(self):
        # piirtää pelin pohjan
        for j in range(0,10):
            for i in range(0,10):
                pygame.draw.rect(self.window,(255,255,255), (i*(self.width + self.margin) + self.margin, j * (self.height + self.margin) + self.margin, self.width, self.height))

    def place_mines(self):
        # luodaan ensin kaksiuloitteinen miinakartta vastaamaan pelin pohjaruudukkoa ja 
        # asetetaan miinat satunnaisesti generoiduille paikoille
        self.minemap = [[0 for x in range(10)] for y in range(10)]
        mines = 0
        while mines < 10:
            x = randint(0,9)
            y = randint(0,9)
            if self.minemap[x][y] == 0:
                self.minemap[x][y] = 10
                mines += 1
        # asetetaan miinoista kertovat vihjeet miinojen viereisiin ruutuihin
        for j in range(0,10):
            for i in range(0,10): # i = y, j = x
                if self.minemap[j][i] == 10: # (y-1,x-1);(y-1,x);(y-1,x+1);(y,x-1);(y,x+1);(y+1,x-1);(y+1,x);(y+1,x+1)
                    if j-1 >= 0 and i-1 >= 0:
                        if self.minemap[j-1][i-1] != 10:
                            self.minemap[j-1][i-1] += 1 # viistoon vasemmalle ylös
                    if i-1 >= 0:
                        if self.minemap[j][i-1] != 10: 
                            self.minemap[j][i-1] += 1 # suoraan ylös
                    if j+1 < 10 and i-1 >= 0:
                        if self.minemap[j+1][i-1] != 10:
                            self.minemap[j+1][i-1] += 1 # viistoon oikealle ylös
                    if j-1 >= 0:
                        if self.minemap[j-1][i] != 10:
                            self.minemap[j-1][i] += 1 # vasen
                    if j+1 < 10:
                        if self.minemap[j+1][i] != 10:
                            self.minemap[j+1][i] += 1 # oikea
                    if j-1 >= 0 and i+1 < 10:
                        if self.minemap[j-1][i+1] != 10:
                            self.minemap[j-1][i+1] += 1 # viistoon vasemmalle alas
                    if i+1 < 10:
                        if self.minemap[j][i+1] != 10:
                            self.minemap[j][i+1] += 1 # suoraan alas
                    if j+1 < 10 and i+1 < 10:
                        if self.minemap[j+1][i+1] != 10:
                            self.minemap[j+1][i+1] += 1 # viistoon oikealle alas

    def open(self):
        self.opened = [[False for x in range(10)] for y in range(10)]

    def dfs(self,y,x):
        if y < 0 or x < 0 or y >= 10 or x >= 10:
            return
        if self.opened[x][y]:
            return
        if  0 < self.minemap[x][y] < 10:
            self.opened[x][y] = True
            return
        self.opened[x][y] = True
        self.dfs(y-1,x-1)
        self.dfs(y-1,x)
        self.dfs(y-1,x+1)
        self.dfs(y,x-1)
        self.dfs(y,x+1)
        self.dfs(y+1,x-1)
        self.dfs(y+1,x)
        self.dfs(y+1,x+1)

    def loop(self):
        while True:
            self.search_events()
            self.draw_window()

    def search_events(self):
        self.gameover = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                y = event.pos[0] // (self.width + self.margin)
                x = event.pos[1] // (self.height + self.margin)
                if not self.gameover:
                    if event.button == 1:
                        if not self.opened[x][y]:
                            if self.minemap[x][y] != 10:
                                self.dfs(y,x)
                                for y in range(0,10):
                                    for x in range(0,10):
                                        if self.opened[x][y]:
                                            pygame.draw.rect(self.window,(128,128,128), (y*(self.width + self.margin) + self.margin, x * (self.height + self.margin) + self.margin, self.width, self.height))
                                            font = pygame.font.SysFont("Arial", 20)
                                            get_number = self.minemap[x][y]
                                            if get_number == 0:
                                                number = font.render("", True, (0,0,255))
                                            else:
                                                number = font.render(str(get_number), True, (0,0,255))
                                            self.window.blit(number,(self.margin+(y*20)+(y*5)+4,self.margin+(x*20)+(x*5)-2))

                            else:
                                pygame.draw.rect(self.window,(255,0,0), (y*(self.width + self.margin) + self.margin, x * (self.height + self.margin) + self.margin, self.width, self.height))
                                font = pygame.font.SysFont("Arial", 40)
                                mine = font.render("*", True, (0,0,0))
                                self.window.blit(mine,(self.margin+(y*20)+(y*5)+3,self.margin+(x*20)+(x*5)-4))
                                self.gameover = True
                    if event.button == 3:
                        font = pygame.font.SysFont("Arial", 20)
                        doubt = font.render("?", True, (0,0,255))
                        self.window.blit(doubt,(self.margin+(y*20)+(y*5)+4,self.margin+(x*20)+(x*5)-2))

    def draw_window(self):
        pygame.display.flip()

if __name__ == "__main__":
    Minesweeper()