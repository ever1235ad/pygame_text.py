import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Draw picture")
my_font = pygame.font.Font(None,40)
white = 255,255,255
blue = 0,0,255
image_rect = pygame.Rect(600,600,100,100)
#rect = image_rect.get_rect()

text_image = my_font.render("Hello,pygame",True,white)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.fill(blue)
        pygame.draw.rect(screen,white,image_rect)
        pygame.draw.circle(screen,white,(300,300),50,2)
        screen.blit(text_image,(100,300))
        pygame.display.update()
      
