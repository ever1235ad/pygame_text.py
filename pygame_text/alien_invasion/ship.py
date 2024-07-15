import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.screen =ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings=ai_game.settings
        #self.setting=settings.Settings()#将settings类里的飞船速度导入
        #self.screen_rect=ai_game.screen.get_rect()
        self.original_image=pygame.image.load('images/12345678.png')
        new_width=60
        new_height=50
        self.image=pygame.transform.scale(self.original_image,(new_width,new_height))
        self.rect=self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
    def update(self):
        if self.moving_right and self.rect.right<=self.settings.screen_width:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left>=0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top>=0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom<=self.settings.screen_height:    #跟ai_game.screen一样
            self.y += self.settings.ship_speed
        self.rect.x=self.x
        self.rect.y=self.y
        
    #def center_ship(self):
        #self.rect
        #self.x = float(self.rect.x)
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)