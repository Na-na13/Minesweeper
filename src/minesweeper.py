from random import randint
from time import time
import pygame
import solver_bot
import ui
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

CELL_SIZE = 20
MARGIN = 5

class Minesweeper:

    def __init__(self,w,h,mines):
        """[summary]

        Args:
            w ([type]): [description]
            h ([type]): [description]
            mines ([type]): [description]
        """
        pygame.init()
        self.mines = mines
        self.minemap = [[0 for a in range(w)] for b in range(h)]
        self.win_height = (CELL_SIZE * h) + (MARGIN * h) + MARGIN + 20
        self.win_width = (CELL_SIZE * w) + (MARGIN * w) + MARGIN
        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        self.window.fill((0,0,0))

        self.draw_grid(w,h)
        self.place_mines(w,h)
        self.place_hints(w,h)

    def draw_grid(self,w,h):
        # piirtää pelin pohjan
        for j in range(0,h):
            for i in range(0,w):
                pygame.draw.rect(self.window,(255,255,255), (i * (CELL_SIZE + MARGIN) + MARGIN, j * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE))

    def place_mines(self,w,h):
        # asetetaan miinat satunnaisesti generoiduille paikoille kaksiulotteiseen miinakarttaan,
        # joka vastaa pelin pohjaruudukkoa
        mines = 0
        while mines < self.mines:
            y = randint(0,h-1) #rivit
            x = randint(0,w-1) #kolumnit
            if self.minemap[y][x] == 0:
                self.minemap[y][x] = 10
                mines += 1

    def place_hints(self,w,h):
        # asetetaan miinoista kertovat vihjeet miinojen naapuriruutuihin
        for j in range(0,h):
            for i in range(0,w): # j = y, i = x
                if self.minemap[j][i] == 10: # (y-1,x-1);(y-1,x);(y-1,x+1);(y,x-1);(y,x+1);(y+1,x-1);(y+1,x);(y+1,x+1)
                    if j-1 >= 0 and i-1 >= 0:
                        if self.minemap[j-1][i-1] != 10:
                            self.minemap[j-1][i-1] += 1 # viistoon vasemmalle ylös
                    if j-1 >= 0:
                        if self.minemap[j-1][i] != 10:
                            self.minemap[j-1][i] += 1 # suoraan ylös
                    if j-1 >= 0 and i+1 < w:
                        if self.minemap[j-1][i+1] != 10:
                            self.minemap[j-1][i+1] += 1 # viistoon oikealle ylös
                    if i-1 >= 0:
                        if self.minemap[j][i-1] != 10:
                            self.minemap[j][i-1] += 1 # vasen
                    if i+1 < w:
                        if self.minemap[j][i+1] != 10:
                            self.minemap[j][i+1] += 1 # oikea
                    if j+1 < h and i-1 >= 0:
                        if self.minemap[j+1][i-1] != 10:
                            self.minemap[j+1][i-1] += 1 # viistoon vasemmalle alas
                    if j+1 < h:
                        if self.minemap[j+1][i] != 10:
                            self.minemap[j+1][i] += 1 # suoraan alas
                    if j+1 < h and i+1 < w:
                        if self.minemap[j+1][i+1] != 10:
                            self.minemap[j+1][i+1] += 1 # viistoon oikealle alas

    def __str__(self):
        # Tulostaa miinojen määrän
        mines = 0
        for y in range(len(self.minemap)):
            for x in range(len(self.minemap[0])):
                if self.minemap[x][y] == 10:
                    mines += 1
        return f"Mines: {mines}"

class MSGameLoop:

    def __init__(self,game,w,h,solver = None):
        self.game = game
        self.solver = solver
        self.opened = [[False for x in range(w)] for y in range(h)]
        self.doubted = [[False for x in range(w)] for y in range(h)]
        self.clock = pygame.time.Clock()
        self.gameover = False
        self.gamewin = False
        self.first_click = True
        self.start_time = 0
        self.end_time = 0
        self.minecounter = game.mines

    def start(self,w,h):
        while True:
            if not self.gameover:
                next_move = self.solver.next_move()
                for move in next_move:
                    print(move.pos,move.button)
            else:
                next_move = []
            for event in pygame.event.get() + next_move:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN: # avataan klikattu ruutu
                    if self.first_click:
                        self.start_time = time()
                        self.first_click = False
                    x = event.pos[0] // (CELL_SIZE + MARGIN)
                    y = event.pos[1] // (CELL_SIZE + MARGIN)
                    if not self.gameover:
                        if event.button == 1:
                            if not self.opened[y][x]:
                                if self.game.minemap[y][x] != 10: # jos ruudussa ei ole miinaa
                                    self.dfs(y,x,w,h)
                                    self.open_cells(w,h)
                                    if self.is_won(w,h):
                                        self.gameover = True
                                        self.gamewin = True
                                        self.end_time = time()
                                        self.win(w,h)
                                        continue
                                        #voitto
                                else: # jos ruudussa on miina
                                    pygame.draw.rect(self.game.window,(255,0,0), (x * (CELL_SIZE + MARGIN) + MARGIN, y * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE))
                                    font = pygame.font.SysFont("Arial", 40)
                                    mine = font.render("*", True, (0,0,0))
                                    self.game.window.blit(mine,(MARGIN + (x * 20) + (x * 5) + 3, MARGIN + (y * 20) + (y * 5) - 4))
                                    self.gameover = True
                                    self.mine_explosion(w,h)
                                    self.end_time = time()
                                    continue
                        elif event.button == 3: # miinaepäilyn merkintä
                            if not self.opened[y][x]:
                                font = pygame.font.SysFont("Arial", 20)
                                if not self.doubted[y][x]:
                                    doubt = font.render("?", True, (0,0,255))
                                    self.game.window.blit(doubt,(MARGIN + (x * 20) + (x * 5) + 4, MARGIN + (y * 20) + (y * 5) - 2))
                                    self.doubted[y][x] = True
                                    self.minecounter -= 1
                                else:
                                    pygame.draw.rect(self.game.window,(255,255,255), (x * (CELL_SIZE + MARGIN) + MARGIN, y * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE))
                                    empty = font.render("", True, (0,0,255))
                                    self.game.window.blit(empty,(MARGIN + (x * 20) + (x * 5) + 4, MARGIN + (y * 20) + (y * 5) - 2))
                                    self.doubted[y][x] = False
                                    self.minecounter += 1
                                    pygame.display.update()
                    #else:
                    #    play_time = f"{self.end_time - self.start_time:.2f}"
                    #    if self.gamewin:
                    #        ui.WinWindow(w,h,self.game.mines,play_time)
                    #    else:
                    #        ui.EndWindow(w,h,self.game.mines,play_time)

            #font = pygame.font.SysFont("Arial", 20)
            #mine = font.render(f"*: {self.minecounter}", True, (255,0,0))
            #self.game.window.blit(mine,(0, (self.game.win_height-20)))    
            pygame.display.flip()
            self.clock.tick(60)

    def dfs(self,y,x,w,h):
        # käydään syvyyshaulla läpi klikatun ruudun naapuriruudut jne, ja merkataan avatuiksi kaikki
        # vierekkäiset ruudut, joiden arvo on < 10 ja lopetetaan haku, jos arvo on > 0 mutta < 10
        if y < 0 or x < 0 or y >= h or x >= w:
            return
        if self.opened[y][x]:
            return
        if  0 < self.game.minemap[y][x] < 10:
            self.opened[y][x] = True
            if self.solver != None:
                self.solver.gamegrid[y][x] = self.game.minemap[y][x]
                #print(self.solver.gamegrid)
            return
        self.opened[y][x] = True
        if self.solver != None:
            self.solver.gamegrid[y][x] = self.game.minemap[y][x]
            #print(self.solver.gamegrid)
        self.dfs(y-1,x-1,w,h)
        self.dfs(y-1,x,w,h)
        self.dfs(y-1,x+1,w,h)
        self.dfs(y,x-1,w,h)
        self.dfs(y,x+1,w,h)
        self.dfs(y+1,x-1,w,h)
        self.dfs(y+1,x,w,h)
        self.dfs(y+1,x+1,w,h)

    def open_cells(self,w,h):
        # piirtää avatuiksi kaikki avatut ruudut
        for a in range(h):
            for b in range(w):
                if self.opened[a][b]:
                    pygame.draw.rect(self.game.window,(128,128,128), (b * (CELL_SIZE + MARGIN) + MARGIN, a * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE))
                    font = pygame.font.SysFont("Arial", 20)
                    get_number = self.game.minemap[a][b]
                    if get_number == 0:
                        number = font.render("", True, (0,0,255))
                    else:
                        number = font.render(str(get_number), True, (0,0,255))
                    self.game.window.blit(number,(MARGIN + (b * 20) + (b * 5) + 4, MARGIN + (a * 20) + (a * 5) - 2))

    def mine_explosion(self,w,h):
        # kun on klikattu miinaa, räjäytetään kaikki miinat
        for y in range(h):
            for x in range(w):
                if self.game.minemap[y][x] == 10:
                    pygame.draw.rect(self.game.window,(255,0,0), (x * (CELL_SIZE + MARGIN) + MARGIN, y * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE))
                    font = pygame.font.SysFont("Arial", 40)
                    mine = font.render("*", True, (0,0,0))
                    self.game.window.blit(mine, (MARGIN + (x * 20) + (x * 5) + 3, MARGIN + (y * 20) + (y * 5) - 4))
                elif self.doubted[y][x] and not self.opened[y][x]: # jos epäilty ei ole miina, laitetaan punainen x
                    font = pygame.font.SysFont("Arial", 20)
                    fail = font.render("X", True, (255,0,0))
                    self.game.window.blit(fail, (MARGIN + (x * 20) + (x * 5) + 4, MARGIN + (y * 20) + (y * 5) - 2))

    def is_won(self,w,h):
        # tarkistetaan jokaisen klikkauksen jälkeen onko voitettu
        for i in range(h):
            for j in range(w):
                if self.opened[i][j] == False and self.game.minemap[i][j] != 10:
                    return False 
        return True

    def win(self,w,h):
        # jos peli voitetaan, piirtää kaikkien miinojen kohdalle vihreän ruudun
        for y in range(h):
            for x in range(w):
                if self.game.minemap[y][x] == 10:
                    pygame.draw.rect(self.game.window,(0,250,0), (x * (CELL_SIZE + MARGIN) + MARGIN, y * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE))


if __name__ == "__main__":
    easy = (10,10,10)
    normal = (16,16,40)
    hard = (30,16,99)
    Minesweeper(10,10,10)
