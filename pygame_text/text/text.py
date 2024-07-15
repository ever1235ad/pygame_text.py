import pygame
import sys
from  mysprite import Mysprite
pygame.init()
screen = pygame.display.set_mode((800,600))
sprite_1 = Mysprite(1,(500,400), -1)

sprite_2 = Mysprite(2,(0,400),1)
group_1 = pygame.sprite.Group()
group_2 = pygame.sprite.Group()
group_1.add(sprite_1)
group_2.add(sprite_2)
pygame.display.set_caption("Escape the dragon")
clock = pygame.time.Clock()

while True:
    for evnet in pygame.event.get():
        if evnet.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #main code
    screen.fill((255,255,255))
    sprite_1.update()
    sprite_2.update()
    if pygame.sprite.groupcollide(group_2,group_1,False,False):
        print("Colldision")
   # screen.blit(sprite_1.image,(sprite_1.x,sprite_1.y))
    #screen.blit(sprite_2.image,(sprite_2.x,sprite_2.y))
    group_1.draw(screen)
    group_2.draw(screen)
    clock.tick(30)
    pygame.display.update()
    