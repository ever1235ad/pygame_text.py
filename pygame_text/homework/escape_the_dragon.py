import pygame,time,sys
class Escape_the_dragon:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800,1200))
        pygame.display.set_caption("Escape the dragon")
        self.screen.draw()
    