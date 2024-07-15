import math
import pygame
import sys
import time
def draw_arc(x,y,width,height,arc1,arc2,color):
    pos = x,y,width,height
    start_angle = math.radians(arc1)
    end_angle = math.radians(arc2) 
    pygame.draw.arc(screen,color,pos,start_angle,end_angle,5)
    
def draw_line (x1,y1,x2,y2,color):
    start_point = (x1,y1)
    end_point = (x2,y2)
    pygame.draw.line(screen,color,start_point,end_point,5)
    
def draw_digit(screen,color):
    myfont = pygame.font.Font(None,60)
    font1_image = myfont.render("1",True,color)
    pos2 = 535,265
    font2_image = myfont.render("2",True,color)
    pos1 = 265,265
    font3_image = myfont.render("3",True,color)
    pos3 = 265,535
    font4_image = myfont.render("4",True,color)
    pos4 = 535,535
    screen.blit(font1_image,pos1)
    screen.blit(font2_image,pos2)
    screen.blit(font3_image,pos3)
    screen.blit(font4_image,pos4)
    
def event_check(flag,color):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                draw_arc(150,150,500,250,0,90,color)
                draw_line(400,150,400,400,color)
                draw_line(400,400,650,400,color)
                flag[0] = 1
            if event.key == pygame.K_1:
                draw_arc(150,150,500,250,90,180,color)
                draw_line(400,150,400,400,color)
                draw_line(150,400,400,400,color)
                flag[1] = 1
            if event.key == pygame.K_3:
                draw_arc(150,400,500,250,180,270,color)
                draw_line(150,400,400,400,color)
                draw_line(400,400,400,650,color)
                flag[2] = 1
            if event.key == pygame.K_4:
                draw_arc(150,400,500,250,270,360,color)
                draw_line(400,400,400,650,color)
                draw_line(400,400,650,400,color)
                flag[3] = 1


def win_game(color):
    draw_arc(150,150,500,250,0,180,color)
    draw_line(400,150,400,400,color)
    draw_line(400,400,650,400,color)
    draw_arc(150,150,500,250,90,180,color)
    draw_line(400,150,400,400,color)
    draw_line(150,400,400,400,color)
    draw_arc(150,400,500,250,180,270,color)
    draw_line(150,400,400,400,color)
    draw_line(400,400,400,650,color)
    draw_arc(150,400,500,250,270,360,color)
    draw_line(400,400,400,650,color)
    draw_line(400,400,650,400,color)
   
pygame.init() 
color1 = (255,255,255)
color2 = (0,255,0)
flag = [0,0,0,0]
screen = pygame.display.set_mode((800,800))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    draw_digit(screen,color1)
    event_check(flag,color1)
    if flag[0] and flag[1] and flag[2] and flag[3] :
       win_game(color2)
    pygame.display.flip()
    



    