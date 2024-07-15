import pygame
import sys
pygame.init()
#init 属性初始化
colck = pygame.time.Clock()
last_time = 0
rate = 30
x = 300
y = 300
v_y = 1
a_y = 1
n = 1
ticks = 20
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("The Animation")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #main code
    image = pygame.image.load(f"Imitater_spin{n}.png")#.convert_alpha()
    image_width = image.get_width()
    image_height = image.get_height()
    image_rect = pygame.Rect(x,y,image_width,image_height)
    scaled_image = pygame.transform.smoothscale(image,(2 * image_width,2 * image_height))
    current_time = pygame.time.get_ticks()
    screen.fill((255,255,255))
    if current_time - last_time >= rate:
        n += 1
        if n >= 6:
            n = 1
        current_time = last_time
        screen.blit(scaled_image,image_rect)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                ticks = 60
            if event.key == pygame.K_w:
                ticks = 20
            if event.key == pygame.K_e:
                ticks = 110
    if ticks == 110:
        y -= v_y
        v_y += a_y
        
    colck.tick(ticks)
    pygame.display.update()