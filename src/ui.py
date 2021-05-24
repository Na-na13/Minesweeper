# Ui
import pygame
from minesweeper import Minesweeper

class StartWindow:

    def __init__(self):
        pygame.init()

        self.win_height = 275
        self.win_width = 255

        
        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        self.window.fill((255,255,255))
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
                pygame.draw.rect(self.window,(170,170,170), (77, 62, 100, 50)) #left,top,w,h
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 62, 100, 50))
            if 117 < mouse[1] < 117+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window,(170,170,170), (77, 117, 100, 50))
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 117, 100, 50))
            if 172 < mouse[1] < 172+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window,(170,170,170), (77, 172, 100, 50))
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
        self.window.fill((255,255,255))
        pygame.display.set_caption("Minesweeper")
        pygame.display.flip()

        clock = pygame.time.Clock()
        while True:
            mouse = pygame.mouse.get_pos()
            if 62 < mouse[1] < 62+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window,(170,170,170), (77, 62, 100, 50)) #left,top,w,h
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 62, 100, 50))
            if 117 < mouse[1] < 117+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window,(170,170,170), (77, 117, 100, 50))
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 117, 100, 50))
            if 172 < mouse[1] < 172+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window,(170,170,170), (77, 172, 100, 50))
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
                            Minesweeper(10,10,10)
                        elif 117 < mouse[1] < 117+50 and 77 < mouse[0] < 77+100:
                            Minesweeper(16,16,40)
                        elif 172 < mouse[1] < 172+50 and 77 < mouse[0] < 77+100:
                            Minesweeper(30,16,99)
                    

            pygame.display.flip()
            clock.tick(60)

class EndWindow:

    def __init__(self):
        pass

if __name__ == "__main__":
    #StartWindow()
    Levels()
