import os

import pygame
import minesweeper
import solver_bot



WHITE = (255,255,255)
DGREY = (128,128,128)
LGREY = (170,170,170)
BLACK = (0,0,0)

class StartWindow:

    def __init__(self):
        os.environ['SDL_AUDIODRIVER'] = 'dsp'
        pygame.init()

        self.win_height = 275
        self.win_width = 255
        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        self.window.fill(WHITE)
        pygame.display.set_caption("Minesweeper")


        clock = pygame.time.Clock()
        done = False
        while not done:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 172 < mouse[1] < 172+50 and 77 < mouse[0] < 77+100:
                        exit()
                    if 62 < mouse[1] < 62+50 and 77 < mouse[0] < 77+100:
                        done = True
                        Levels()

            if 62 < mouse[1] < 62+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window, LGREY, (77, 62, 100, 50)) #left,top,w,h
            else:
                pygame.draw.rect(self.window, DGREY, (77, 62, 100, 50))
            if 117 < mouse[1] < 117+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window, LGREY, (77, 117, 100, 50))
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 117, 100, 50))
            if 172 < mouse[1] < 172+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window, LGREY, (77, 172, 100, 50))
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 172, 100, 50))

            font = pygame.font.SysFont("Arial", 40)
            text = font.render("PLAY", True, (0,0,0))
            self.window.blit(text,((62+(50/2)), (15+(100/2))))

            font = pygame.font.SysFont("Arial", 40)
            text = font.render("QUIT", True, (0,0,0))
            self.window.blit(text,((62+(50/2)), (125+(100/2))))

            font = pygame.font.SysFont("Arial", 40)
            text = font.render("MINESWEEPER", True, (0,0,0))
            self.window.blit(text,(2, 0))

            pygame.display.flip()
            clock.tick(60)

class Levels:

    def __init__(self):
        pygame.init()

        self.win_height = 275
        self.win_width = 255
        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        self.window.fill(WHITE)
        pygame.display.flip()

        self.clock = Clock()
        while True:
            mouse = pygame.mouse.get_pos()
            if 62 < mouse[1] < 62+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window, LGREY, (77, 62, 100, 50)) #left,top,w,h
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 62, 100, 50))
            if 117 < mouse[1] < 117+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window, LGREY, (77, 117, 100, 50))
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 117, 100, 50))
            if 172 < mouse[1] < 172+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window, LGREY, (77, 172, 100, 50))
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 172, 100, 50))

            font = pygame.font.SysFont("Arial", 40)
            text = font.render("EASY", True, (0,0,0))
            self.window.blit(text,((55+(50/2)), (15+(100/2))))

            font = pygame.font.SysFont("Arial", 27)
            text = font.render("NORMAL", True, (0,0,0))
            self.window.blit(text,((55+(50/2)), (77+(100/2))))

            font = pygame.font.SysFont("Arial", 40)
            text = font.render("HARD", True, (0,0,0))
            self.window.blit(text,((55+(50/2)), (125+(100/2))))

            font = pygame.font.SysFont("Arial", 40)
            text = font.render("LEVELS", True, (0,0,0))
            self.window.blit(text,((255/4), 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 62 < mouse[1] < 62+50 and 77 < mouse[0] < 77+100:
                            game = minesweeper.Minesweeper(10,10,10)
                            bot = solver_bot.SolverBot(10,10,10,game) # tämä on bottia varten
                            gameloop = minesweeper.MSGameLoop(game,10,10,bot) # tämä on bottia varten
                            #gameloop = minesweeper.MSGameLoop(game,10,10)
                            gameloop.start(10,10)
                        elif 117 < mouse[1] < 117+50 and 77 < mouse[0] < 77+100:
                            game = minesweeper.Minesweeper(16,16,40)
                            bot = solver_bot.SolverBot(16,16,40,game) # tämä on bottia varten
                            gameloop = minesweeper.MSGameLoop(game,16,16,bot) # tämä on bottia varten
                            #gameloop = minesweeper.MSGameLoop(game,16,16)
                            gameloop.start(16,16)
                        elif 172 < mouse[1] < 172+50 and 77 < mouse[0] < 77+100:
                            game = minesweeper.Minesweeper(30,16,99)
                            bot = solver_bot.SolverBot(30,16,99,game) # tämä on bottia varten
                            #gameloop = minesweeper.MSGameLoop(game,30,16,bot) # tämä on bottia varten
                            gameloop = minesweeper.MSGameLoop(game,30,16)
                            gameloop.start(30,16)

            pygame.display.flip()
            self.clock.tick(60)

class EndWindow:

    def __init__(self,w,h,mines,play_time):
        pygame.init()

        self.win_height = 275
        self.win_width = 255
        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        self.window.fill(WHITE)
        self.clock = Clock()
        self.time = play_time

        while True:
            mouse = pygame.mouse.get_pos()
            if 62 < mouse[1] < 62+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window, LGREY, (77, 62, 100, 50)) #left,top,w,h
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 62, 100, 50))
            if 117 < mouse[1] < 117+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window, LGREY, (77, 117, 100, 50))
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 117, 100, 50))
            if 172 < mouse[1] < 172+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window, LGREY, (77, 172, 100, 50))
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 172, 100, 50))

            font = pygame.font.SysFont("Arial", 40)
            text = font.render("RETRY", True, (0,0,0))
            self.window.blit(text,((55+(50/2)), (15+(100/2))))

            font = pygame.font.SysFont("Arial", 27)
            text = font.render("CHANGE LEVEL", True, (0,0,0))
            self.window.blit(text,((55+(50/2)), (77+(100/2))))

            font = pygame.font.SysFont("Arial", 40)
            text = font.render("QUIT", True, (0,0,0))
            self.window.blit(text,((55+(50/2)), (125+(100/2))))

            font = pygame.font.SysFont("Arial", 40)
            text = font.render("YOU LOSE" + self.time, True, (0,0,0))
            self.window.blit(text,(0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 62 < mouse[1] < 62+50 and 77 < mouse[0] < 77+100:
                            game = minesweeper.Minesweeper(w,h,mines)
                            gameloop = minesweeper.MSGameLoop(game,w,h)
                            gameloop.start(w,h)
                        elif 117 < mouse[1] < 117+50 and 77 < mouse[0] < 77+100:
                            Levels()
                        elif 172 < mouse[1] < 172+50 and 77 < mouse[0] < 77+100:
                            exit()

            pygame.display.flip()
            self.clock.tick(60)

class WinWindow:
    
    def __init__(self,w,h,mines,play_time):
        pygame.init()

        self.win_height = 275
        self.win_width = 255
        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        self.window.fill(WHITE)
        self.clock = Clock()
        self.time = play_time

        while True:
            mouse = pygame.mouse.get_pos()
            if 62 < mouse[1] < 62+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window, LGREY, (77, 62, 100, 50)) #left,top,w,h
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 62, 100, 50))
            if 117 < mouse[1] < 117+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window, LGREY, (77, 117, 100, 50))
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 117, 100, 50))
            if 172 < mouse[1] < 172+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window, LGREY, (77, 172, 100, 50))
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 172, 100, 50))

            font = pygame.font.SysFont("Arial", 40)
            text = font.render("RETRY", True, (0,0,0))
            self.window.blit(text,((55+(50/2)), (15+(100/2))))

            font = pygame.font.SysFont("Arial", 27)
            text = font.render("CHANGE LEVEL", True, (0,0,0))
            self.window.blit(text,((55+(50/2)), (77+(100/2))))

            font = pygame.font.SysFont("Arial", 40)
            text = font.render("QUIT", True, (0,0,0))
            self.window.blit(text,((55+(50/2)), (125+(100/2))))

            font = pygame.font.SysFont("Arial", 40)
            text = font.render("YOU WIN!" + self.time, True, (0,0,0))
            self.window.blit(text,(0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 62 < mouse[1] < 62+50 and 77 < mouse[0] < 77+100:
                            game = minesweeper.Minesweeper(w,h,mines)
                            gameloop = minesweeper.MSGameLoop(game,w,h)
                            gameloop.start(w,h)
                        elif 117 < mouse[1] < 117+50 and 77 < mouse[0] < 77+100:
                            Levels()
                        elif 172 < mouse[1] < 172+50 and 77 < mouse[0] < 77+100:
                            exit()

            pygame.display.flip()
            self.clock.tick(60)

class Clock:

    def __init__(self):
        self.clock = pygame.time.Clock()

    def tick(self, fps):
        self.clock.tick(fps)

    def get_ticks(self):
        return pygame.time.get_ticks()

if __name__ == "__main__":
    StartWindow()
    #Levels()
