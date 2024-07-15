import pygame
import time
import random
from pygame.sprite import Sprite
class Bomb(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.removed_bomb = ai_game.removed_bomb
        self.red = 255,0,0
        self.font = pygame.font.Font(None,100)
        self.radius = random.randint(10,100)
        self.x = random.randint(self.radius,1000 - 2*self.radius)
        self.y = self.radius    
        self.speed =  1.0  
        
    def update(self):
        self.y += self.speed
        pygame.draw.circle(self.screen,self.red,(self.x,self.y),self.radius,0)        

              
            

            
        
        
        
        
        
        