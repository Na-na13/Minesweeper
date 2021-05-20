# Minesweeper
import pygame
from random import randint

class Minesweeper:

    def __init__(self,w,h,mines):
        self.mines = mines
        #self.x = x
        #self.y = y

        pygame.init()

        self.margin = 5
        self.height = 20
        self.width = 20
        self.win_height = (self.height*h) + (self.margin*h)+self.margin
        self.win_width = (self.width*w) + (self.margin*w)+self.margin

        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        self.window.fill((0,0,0))
        pygame.display.set_caption("Minesweeper")

        self.draw_grid(w,h)
        self.place_mines(w,h)
        self.open(w,h)
        self.loop(w,h)


    def draw_grid(self,w,h):
        # piirtää pelin pohjan
        for j in range(0,h):
            for i in range(0,w):
                pygame.draw.rect(self.window,(255,255,255), (i*(self.width + self.margin) + self.margin, j * (self.height + self.margin) + self.margin, self.width, self.height))

    def place_mines(self,w,h):
        # luodaan ensin kaksiuloitteinen miinakartta vastaamaan pelin pohjaruudukkoa ja 
        # asetetaan miinat satunnaisesti generoiduille paikoille
        self.minemap = [[0 for a in range(w)] for b in range(h)]
        mines = 0
        while mines < self.mines:
            x = randint(0,h-1) #rivit
            y = randint(0,w-1) #kolumnit
            if self.minemap[x][y] == 0:
                self.minemap[x][y] = 10
                mines += 1
        # asetetaan miinoista kertovat vihjeet miinojen viereisiin ruutuihin
        for j in range(0,h):
            for i in range(0,w): # i = y, j = x
                if self.minemap[j][i] == 10: # (y-1,x-1);(y-1,x);(y-1,x+1);(y,x-1);(y,x+1);(y+1,x-1);(y+1,x);(y+1,x+1)
                    if j-1 >= 0 and i-1 >= 0:
                        if self.minemap[j-1][i-1] != 10:
                            self.minemap[j-1][i-1] += 1 # viistoon vasemmalle ylös
                    if i-1 >= 0:
                        if self.minemap[j][i-1] != 10: 
                            self.minemap[j][i-1] += 1 # suoraan ylös
                    if j+1 < h and i-1 >= 0:
                        if self.minemap[j+1][i-1] != 10:
                            self.minemap[j+1][i-1] += 1 # viistoon oikealle ylös
                    if j-1 >= 0:
                        if self.minemap[j-1][i] != 10:
                            self.minemap[j-1][i] += 1 # vasen
                    if j+1 < h:
                        if self.minemap[j+1][i] != 10:
                            self.minemap[j+1][i] += 1 # oikea
                    if j-1 >= 0 and i+1 < w:
                        if self.minemap[j-1][i+1] != 10:
                            self.minemap[j-1][i+1] += 1 # viistoon vasemmalle alas
                    if i+1 < w:
                        if self.minemap[j][i+1] != 10:
                            self.minemap[j][i+1] += 1 # suoraan alas
                    if j+1 < h and i+1 < w:
                        if self.minemap[j+1][i+1] != 10:
                            self.minemap[j+1][i+1] += 1 # viistoon oikealle alas

    def open(self,w,h):
        self.opened = [[False for x in range(w)] for y in range(h)]

    def dfs(self,y,x,w,h):
        # käydään syvyyshaulla läpi klikatun ruudun naapuriruudut jne, ja merkataan avatuiksi kaikki vierekkäiset
        # ruudut, joiden arvo on < 10 ja lopetetaan haku, jos arvo on > 0 mutta < 10 
        if y < 0 or x < 0 or y >= w or x >= h:
            return
        if self.opened[x][y]:
            return
        if  0 < self.minemap[x][y] < 10:
            self.opened[x][y] = True
            return
        self.opened[x][y] = True
        self.dfs(y-1,x-1,w,h)
        self.dfs(y-1,x,w,h)
        self.dfs(y-1,x+1,w,h)
        self.dfs(y,x-1,w,h)
        self.dfs(y,x+1,w,h)
        self.dfs(y+1,x-1,w,h)
        self.dfs(y+1,x,w,h)
        self.dfs(y+1,x+1,w,h)

    def loop(self,w,h):
        while True:
            self.search_events(w,h)
            self.draw_window()

    def search_events(self,w,h):
        self.gameover = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # avataan klikattu ruutu
                y = event.pos[0] // (self.width + self.margin)
                x = event.pos[1] // (self.height + self.margin)
                if not self.gameover:
                    if event.button == 1:
                        if not self.opened[x][y]:
                            if self.minemap[x][y] != 10: # jos ruudussa ei ole miinaa
                                self.dfs(y,x,w,h)
                                for a in range(0,h):
                                    for b in range(0,w):
                                        if self.opened[a][b]:
                                            pygame.draw.rect(self.window,(128,128,128), (b*(self.width + self.margin) + self.margin, a * (self.height + self.margin) + self.margin, self.width, self.height))
                                            font = pygame.font.SysFont("Arial", 20)
                                            get_number = self.minemap[a][b]
                                            if get_number == 0:
                                                number = font.render("", True, (0,0,255))
                                            else:
                                                number = font.render(str(get_number), True, (0,0,255))
                                            self.window.blit(number,(self.margin+(b*20)+(b*5)+4,self.margin+(a*20)+(a*5)-2))

                            else: # jos ruudussa on miina
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
    easy = (10,10,10)
    intermediate = (16,16,40)
    hard = (30,16,99)
    Minesweeper(30,16,99)
