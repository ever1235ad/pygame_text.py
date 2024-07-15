import pygame
import math
import sys
pygame.init()
rate = pygame.time.Clock()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Moving rectangle")
rect_x = 0
rect_y = 0
vel_x = 1
vel_y = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255,255,255))
    if rect_x < 0 or rect_x > 900:
        vel_x = -vel_x
    if rect_y < 0 or rect_y > 700:
        vel_y = -vel_y
        breakpoint()
    rect_x += vel_x
    rect_y += vel_y
    pos = rect_x,rect_y,100,100
    color = 255,0,0
    pygame.draw.rect(screen,color,pos)
    pygame.draw.line(screen,color,(100,200),(200,300),1)
    pygame.draw.arc(screen,color,(0,0,200,100),math.radians(0),math.radians(270),1)
    rate.tick(60)
    pygame.display.update()
    
