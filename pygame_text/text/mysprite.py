import pygame
class Mysprite(pygame.sprite.Sprite):
    def __init__(self,frame,pos,flag = 1):
        super().__init__()
        self.frame = frame
        self.image = pygame.image.load(f"Imitater_spin{self.frame}.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.flag = flag
        
    def update(self):
        self.rect.x += self.flag