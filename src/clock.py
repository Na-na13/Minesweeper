import pygame

class Clock:

    def __init__(self):
        self.clock = pygame.time.Clock()

    def tick(self, fps):
        self.clock.tick(fps)
