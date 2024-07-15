import pygame
import sys
pygame.init()
frame = 1
n = 1
x = -180
y = 0
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
#image = pygame.image.load(f"dragon_image/dragon_{frame}.png").convert_alpha()
pygame.display.set_caption("Escape the dragon")
font = pygame.font.Font(None,60)
font_image = font.render("Loading. . .",True,(255,20,153))

while True:
    for evnet in pygame.event.get():
        if evnet.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if frame >= 5:
        n = -1
    if frame <= 1:
        n = 1
    frame += n
    x += 5
    if x >= 180 + 800 - 20:
        x = -180
    image = pygame.image.load(f"dragon_image/dragon_{frame}.png").convert_alpha()
    screen.fill((255,255,255))
    screen.blit(font_image,(300,520))
    screen.blit(image,(x,y))
    clock.tick(8)
    pygame.display.update()
    