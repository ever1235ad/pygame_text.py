import pygame
import math
import sys
pygame.init()
screen = pygame.display.set_mode((800,800))
image = pygame.image.load('jiqiang.png').convert_alpha()
width,height = image.get_size()
clock = pygame.time.Clock()
scaled_image = pygame.transform.smoothscale(image,(width//2,height//2))
pygame.display.set_caption("Text")
radius = 300
pos_o = (400,400)
pos_x = 400
pos_y = 400
angle = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    if angle < 360:
        old_x = pos_x + radius * math.cos(math.radians(angle))
        old_y = pos_y + radius * math.sin(math.radians(angle))
      #  screen.blit(scaled_image,(old_x,old_y))
        new_x = pos_x + radius * math.cos(math.radians(angle+1))
        new_y = pos_y + radius * math.sin(math.radians(angle+1))
        del_x = new_x - old_x
        del_y = new_y - old_y
        rangle = math.atan2(-del_y,del_x)
        rangled = math.degrees(rangle)
        rotated_image = pygame.transform.rotate(scaled_image,rangled)
        screen.blit(rotated_image,(new_x,new_y))
        new_y = old_y
        new_x = old_x
        angle += 1
    if angle >= 360:
        angle = 0
    clock.tick(120)
    pygame.display.update()
    
        
