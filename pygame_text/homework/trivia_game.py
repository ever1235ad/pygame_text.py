import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((1000,800))
myfont = pygame.font.Font(None,60)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    for n in range(3):
       myfont_image = myfont.render(f"question {n}:",True,(0,0,255))
       screen.blit(myfont_image,(100+n*100,100+n*100))
    #screen.fill((255,255,255))
    pygame.display.update()
  