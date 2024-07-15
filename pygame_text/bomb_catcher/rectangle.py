import pygame
class Rectangle():
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.x,self.y = 500,800 - 30
        self.yellow = 255,165,0
        self.width = 300
        self.height = 30
        self.pos = (self.x,self.y,self.width,self.height)
    def move_rec(self):
        x = float(self.x)
        y = float(self.y)
        #keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
                (self.x,self.y) = mouse_pos
                
        '''if keys[pygame.K_a]:
            if x > 0 :
                x -= 1.0
                self.x = x
        if keys[pygame.K_d]:
            if x < 1000 - self.width:
                x += 1.0
                self.x = x'''
        self.pos = (self.x,self.y,self.width,self.height)
        pygame.draw.rect(self.screen,self.yellow,self.pos,0)
        
            
        