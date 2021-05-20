# Ui
import pygame

class MinesweeperUI:

    def __init__(self):
        pygame.init()

        self.win_height = 275
        self.win_width = 255

        
        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        self.window.fill((255,255,255))
        pygame.display.set_caption("Minesweeper")


        clock = pygame.time.Clock()
        while True:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    exit()

            mouse = pygame.mouse.get_pos()

            if 62 < mouse[1] < 62+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window,(0,250,0), (77, 62, 100, 50)) #left,top,w,h
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 62, 100, 50))
            if 117 < mouse[1] < 117+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window,(0,250,0), (77, 117, 100, 50))
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 117, 100, 50))
            if 172 < mouse[1] < 172+50 and 77 < mouse[0] < 77+100:
                pygame.draw.rect(self.window,(0,250,0), (77, 172, 100, 50))
            else:
                pygame.draw.rect(self.window,(128,128,128), (77, 172, 100, 50))
                
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    MinesweeperUI()
