from random import randint
from time import time
import pygame

from ui import EndWindow
from event import Event
from clock import Clock

CELL_SIZE = 20
MARGIN = 5
MINE = 10
WHITE = 255,255,255
BLACK = 0,0,0
GREY = 128,128,128
RED = 255,0,0
GREEN = 0,250,0
BLUE = 0,0,255

class Minesweeper:

    def __init__(self,w,h,mines):
        """Pelikentän alustaminen

        Args:
            w: pelikentän leveys
            h: pelikentän korkeus
            mines: miinojen lukumäärä
        """
        pygame.init()
        self.mines = mines
        self.minemap = [[0 for x in range(w)] for y in range(h)]
        self.win_height = (CELL_SIZE * h) + (MARGIN * h) + MARGIN + 20
        self.win_width = (CELL_SIZE * w) + (MARGIN * w) + MARGIN
        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        self.window.fill(BLACK)
        self.draw_grid(w,h)
        self.place_mines(w,h)
        self.place_hints(w,h)

    def draw_grid(self,w,h):
        """Piirtää pelin pohjan

        Args:
            w: pelikentän leveys
            h: pelikentän korkeus
        """
        for y in range(0, h):
            for x in range(0, w):
                pygame.draw.rect(
                    self.window, WHITE, (x * (CELL_SIZE + MARGIN) + MARGIN,
                    y * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE))

    def place_mines(self,w,h):
        """ Asettaa miinat satunnaisesti valituile paikoille kaksiulotteiseen miinakarttaan,
            joka vastaa pelin pohjaruudukkoa

        Args:
            w: pelikentän leveys
            h: pelikentän korkeus
        """
        mines = 0
        while mines < self.mines:
            y = randint(0, h - 1)
            x = randint(0, w - 1)
            if self.minemap[y][x] == 0:
                self.minemap[y][x] = MINE
                mines += 1

    def place_hints(self,w,h):
        """Asettaan miinoista kertovat vihjeet miinojen naapuriruutuihin

        Args:
            w: pelikentän leveys
            h: pelikentän korkeus
        """
        for y in range(0, h):
            for x in range(0, w):
                if self.minemap[y][x] == MINE:
                    # (y-1,x-1);(y-1,x);(y-1,x+1);(y,x-1);(y,x+1);(y+1,x-1);(y+1,x);(y+1,x+1)
                    if y-1 >= 0 and x-1 >= 0:
                        if self.minemap[y-1][x-1] != MINE:
                            self.minemap[y-1][x-1] += 1 # viistoon vasemmalle ylös
                    if y-1 >= 0:
                        if self.minemap[y-1][x] != MINE:
                            self.minemap[y-1][x] += 1 # suoraan ylös
                    if y-1 >= 0 and x+1 < w:
                        if self.minemap[y-1][x+1] != MINE:
                            self.minemap[y-1][x+1] += 1 # viistoon oikealle ylös
                    if x-1 >= 0:
                        if self.minemap[y][x-1] != MINE:
                            self.minemap[y][x-1] += 1 # vasen
                    if x+1 < w:
                        if self.minemap[y][x+1] != MINE:
                            self.minemap[y][x+1] += 1 # oikea
                    if y+1 < h and x-1 >= 0:
                        if self.minemap[y+1][x-1] != MINE:
                            self.minemap[y+1][x-1] += 1 # viistoon vasemmalle alas
                    if y+1 < h:
                        if self.minemap[y+1][x] != MINE:
                            self.minemap[y+1][x] += 1 # suoraan alas
                    if y+1 < h and x+1 < w:
                        if self.minemap[y+1][x+1] != MINE:
                            self.minemap[y+1][x+1] += 1 # viistoon oikealle alas

    def __str__(self):
        """Laskee miinojen määrän miinakrtassa

        Returns:
            miinojen määrä merkkijono-muodossa
        """
        mines = 0
        for y in range(len(self.minemap)):
            for x in range(len(self.minemap[0])):
                if self.minemap[y][x] == MINE:
                    mines += 1
        return f"Mines: {mines}"

class MSGameLoop:

    def __init__(self,game,w,h,solver = None):
        """Pelisilmukka, jossa päivitetään pelaajan liikkeet näkyviin pelinäkymään

        Args:
            game: pelikenttä-olio miinoine ja vihjeineen
            w: pelikentän leveys
            h: pelikentän korkeus
            solver: pelin ratkaisijabotti-olio, oletusarvo None.
        """
        self.game = game
        self.solver = solver
        self.opened = [[False for x in range(w)] for y in range(h)]
        self.doubted = [[False for x in range(w)] for y in range(h)]
        self.clock = Clock()
        self.gameover = False
        self.gamewin = False
        self.first_click = True
        self.start_time = 0
        self.end_time = 0
        self.minecounter = game.mines

    def start(self,w,h):
        while True:
            if not self.gameover and self.solver is not None:
                next_move = self.solver.next_move()
            else:
                #next_move = [Event(pygame.MOUSEBUTTONDOWN, (115,140),1)] # Testauksen rivi
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
                    if x >= w or y >= h:
                        break
                    if not self.gameover:
                        if event.button == 1: # ruudun avaaminen
                            if not self.opened[y][x]:
                                if self.game.minemap[y][x] != MINE: # jos ruudussa ei ole miinaa
                                    self.dfs(y,x,w,h)
                                    self.open_cells(w,h)
                                    if self.is_won(w,h):
                                        self.gameover = True
                                        self.gamewin = True
                                        self.end_time = time()
                                        self.win(w,h)
                                        continue
                                else: # jos ruudussa on miina
                                    pygame.draw.rect(
                                        self.game.window, RED,
                                        (x * (CELL_SIZE + MARGIN) + MARGIN,
                                        y * (CELL_SIZE + MARGIN) + MARGIN,
                                        CELL_SIZE, CELL_SIZE))
                                    font = pygame.font.SysFont("Arial", 40)
                                    mine = font.render("*", True, BLACK)
                                    self.game.window.blit(
                                        mine,(MARGIN + (x * 20) + (x * 5) + 3,
                                        MARGIN + (y * 20) + (y * 5) - 4))
                                    self.gameover = True
                                    self.end_time = time()
                                    self.mine_explosion(w,h)
                                    continue
                        elif event.button == 3: # miinaepäilyn merkintä
                            if not self.opened[y][x]:
                                font = pygame.font.SysFont("Arial", 20)
                                if not self.doubted[y][x]:
                                    doubt = font.render("?", True, BLUE)
                                    self.game.window.blit(
                                        doubt,(MARGIN + (x * 20) + (x * 5) + 4,
                                        MARGIN + (y * 20) + (y * 5) - 2))
                                    self.doubted[y][x] = True
                                    self.minecounter -= 1
                                else:
                                    pygame.draw.rect(
                                        self.game.window, WHITE,
                                        (x * (CELL_SIZE + MARGIN) + MARGIN,
                                        y * (CELL_SIZE + MARGIN) + MARGIN,
                                        CELL_SIZE, CELL_SIZE))
                                    self.doubted[y][x] = False
                                    self.minecounter += 1
                    else:
                        #return # Testauksen rivi
                        play_time = f"{self.end_time - self.start_time:.2f}"
                        EndWindow(w,h,self.game.mines,play_time,self.gamewin,self.solver)

            self.show_minecounter(w,h)
            pygame.display.update()
            self.clock.tick(60)

    def dfs(self,y,x,w,h):
        """Käydään syvyyshaulla läpi klikatun ruudun naapuriruudut jne,
            ja merkataan avatuiksi kaikki vierekkäiset ruudut, joiden
            arvo on < 10 (MINE) ja lopetetaan haku,
            jos arvo on > 0 mutta < 10 (MINE)

        Args:
            y: y-akselin koordinaatti peliruudukossa
            x: x-akselin koordinaatti peliruudukossa
            w: pelikentän leveys
            h: pelikentän korkeus
        """
        if y < 0 or x < 0 or y >= h or x >= w:
            return
        if self.opened[y][x]:
            return
        if  0 < self.game.minemap[y][x] < 10:
            self.opened[y][x] = True
            if self.solver is not None:
                self.solver.gamegrid[y][x] = self.game.minemap[y][x]
            return
        self.opened[y][x] = True
        if self.solver is not None:
            self.solver.gamegrid[y][x] = self.game.minemap[y][x]
        self.dfs(y-1,x-1,w,h)
        self.dfs(y-1,x,w,h)
        self.dfs(y-1,x+1,w,h)
        self.dfs(y,x-1,w,h)
        self.dfs(y,x+1,w,h)
        self.dfs(y+1,x-1,w,h)
        self.dfs(y+1,x,w,h)
        self.dfs(y+1,x+1,w,h)

    def open_cells(self,w,h):
        """Piirtää pelinäkymään avatuiksi kaikki pelikentän avatut ruudut

        Args:
            w: pelikentän leveys
            h: pelikentän korkeus
        """
        for y in range(h):
            for x in range(w):
                if self.opened[y][x]:
                    pygame.draw.rect(
                        self.game.window, GREY,
                        (x * (CELL_SIZE + MARGIN) + MARGIN,
                        y * (CELL_SIZE + MARGIN) + MARGIN,
                        CELL_SIZE, CELL_SIZE))
                    font = pygame.font.SysFont("Arial", 20)
                    get_number = self.game.minemap[y][x]
                    if get_number == 0:
                        number = font.render("", True, BLUE)
                    else:
                        number = font.render(str(get_number), True, BLUE)
                    self.game.window.blit(
                        number,(MARGIN + (x * 20) + (x * 5) + 4,
                        MARGIN + (y * 20) + (y * 5) - 2))

    def mine_explosion(self,w,h):
        """Kun pelaaja avaa ruudun, jossa on miina, räjäytetään kaikki miinat.
            Jos miinaepäily ei ole oikein, laitetaan väärän epäilyn päälle
            punainen "X"

        Args:
            w: pelikentän leveys
            h: pelikentän korkeus
        """
        for y in range(h):
            for x in range(w):
                if self.game.minemap[y][x] == MINE:
                    pygame.draw.rect(
                        self.game.window, RED,
                        (x * (CELL_SIZE + MARGIN) + MARGIN,
                        y * (CELL_SIZE + MARGIN) + MARGIN,
                        CELL_SIZE, CELL_SIZE))
                    font = pygame.font.SysFont("Arial", 40)
                    mine = font.render("*", True, BLACK)
                    self.game.window.blit(
                        mine, (MARGIN + (x * 20) + (x * 5) + 3,
                        MARGIN + (y * 20) + (y * 5) - 4))
                elif self.doubted[y][x] and not self.opened[y][x]:
                    font = pygame.font.SysFont("Arial", 20)
                    fail = font.render("X", True, RED)
                    self.game.window.blit(
                        fail, (MARGIN + (x * 20) + (x * 5) + 4,
                        MARGIN + (y * 20) + (y * 5) - 2))

    def is_won(self,w,h):
        """Tarkistaa jokaisen ruudun avauksen jälkeen onko peli voitettu

        Args:
            w: pelikentän leveys
            h: pelikentän korkeus

        Returns:
            True, jos voitettu, False, jos ei voitettu
        """
        for y in range(h):
            for x in range(w):
                if self.opened[y][x] is False and self.game.minemap[y][x] != MINE:
                    return False
        return True

    def win(self,w,h):
        """Jos peli voitetaan, piirtää pelinäkymään kaikkien miinojen kohdalle vihreän ruudun

        Args:
            w: pelikentän leveys
            h: pelikentän korkeus
        """
        for y in range(h):
            for x in range(w):
                if self.game.minemap[y][x] == MINE:
                    pygame.draw.rect(
                        self.game.window,GREEN,
                        (x * (CELL_SIZE + MARGIN) + MARGIN,
                        y * (CELL_SIZE + MARGIN) + MARGIN,
                        CELL_SIZE, CELL_SIZE))

    def show_minecounter(self,w,h):
        pygame.draw.rect(
            self.game.window, BLACK,
            (0, (CELL_SIZE*h)+(MARGIN*h),
            (CELL_SIZE*w)+(MARGIN*w),
            (CELL_SIZE*h)+(MARGIN*h)))
        font = pygame.font.SysFont("Arial", 20)
        total = font.render("Mines: " + str(self.minecounter), True, RED)
        self.game.window.blit(total,(0, (self.game.win_height-25)))
