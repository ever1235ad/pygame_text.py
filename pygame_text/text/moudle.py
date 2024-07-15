import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800,600))
image = pygame.image.load("dragon_1")
pygame.display.set_caption("Escape the dragon")

while True:
    for evnet in pygame.event.get():
        if evnet.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #main code
    pygame.display.update()
    