import pygame
class Dragon(pygame.sprite.Sprite):
    def __init__(self,ai_game,framerate):
        super().__init__()
        self.clock = pygame.time.Clock()
        self.screen = ai_game.screen
        self.last_time = 0
        self.framerate = framerate
        self.frame = 1
        self.n = 1
        self.x = 180
        self.y = 520  #dragon_pos
        self.r_image = pygame.image.load("dragon_image/dragon_1.png")
        self.r_img_width = self.r_image.get_width()
        self.r_img_height = self.r_image.get_height()
        self.rect = (self.x,self.y,self.r_img_width,self.r_img_height)

        
    def update(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.last_time >= self.framerate:
            if self.frame >= 5:
                self.n = -1
            if self.frame <= 1:
                self.n = 1
                
            self.frame += self.n
            self.x += 2
            self.last_time = self.current_time
    
            if self.x >= 180 + 800 - 20:
                self.x = -180
        self.image = pygame.image.load(f"dragon_image/dragon_{self.frame}.png")
        self.screen.blit(self.image,(self.x,self.y))