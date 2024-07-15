import pygame
class Fireball(pygame.sprite.Sprite):
    def __init__(self,ai_game,framerate):
        super().__init__()
        self.clock = pygame.time.Clock()
        self.screen = ai_game.screen
        self.screen_width = ai_game.scr_width
        self.framerate = framerate
        self.frame = 0
        self.last_time = 0
        self.init_image = pygame.image.load("data_image/fireball.png")
        self.image = pygame.transform.rotate(self.init_image,180)
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        self.row = 0
        self.frame_width = self.image_width
        self.frame_height = self.image_height // 3
        self.x = self.screen_width
        self.y = 610
        self.v_x = 10
    
    def update(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.last_time >= self.framerate:
            self.frame_img_rect = pygame.Rect(0,self.frame_height * self.row,self.frame_width,self.frame_height)
            self.frame_img = self.image.subsurface(self.frame_img_rect) 
            self.screen.blit(self.frame_img,(self.x,self.y))  #character_pos
            
            self.last_time = self.current_time
            self.row += 1     
            if self.row > 2:
                self.row = 0
            self.x -= self.v_x
            if self.x <= -15:
                self.x = self.screen_width + 10