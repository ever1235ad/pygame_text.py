import pygame
import sys
import random
from rectangle import Rectangle
from bomb import Bomb
class Bomb_catcher():
    def __init__(self):
        pygame.init()
        self.font_s = pygame.font.Font(None,50)
        self.font_b = pygame.font.Font(None,100)
        self.lifes = 3
        self.scores = 0
        self.interval = 1000
        self.removed_bomb = 0
        self.red = 255,0,0
        self.last_time = 0
        self.Bomb = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000,800))    #注意如果要调屏幕大小，请在bomb类里做出相应变化
        self.rec = Rectangle(self)
        self.bomb = Bomb(self)
        pygame.display.set_caption("Bomb Catcher")
        
        
    def print_text(self,font,x,y,text,color):
        font_image = font.render(text,True,color)
        self.screen.blit(font_image,(x,y))
        
    def place_bomb(self):
        self.currrent_time = pygame.time.get_ticks()   
        if self.currrent_time - self.last_time >= self.interval:
            self.interval = 1000 * random.randint(1,4)
            new_bomb = Bomb(self)           #为什么要用Bomb（self）而不能用self.bomb           #######self.bomb是一个已有实例，不是创建新的实例（精灵）##########
            self.Bomb.add(new_bomb)
            self.last_time = self.currrent_time
        #pygame.draw.circle(self.screen,self.red,(self.x,self.y),self.radius,0)
        
    def check_bottom(self):
        for bomb in self.Bomb:
            if bomb.y >= 800:
                self.removed_bomb = bomb
                self.scores -= 5
                self.lifes -= 1
                self.Bomb.remove(bomb)
                
    def check_collision(self):
        for bomb in self.Bomb:
            if bomb.y >= 800 - (bomb.radius + self.rec.height):
                if bomb.x >= self.rec.x - bomb.radius and bomb.x <= self.rec.x + self.rec.width + bomb.radius:
                    self.scores += 10
                    self.Bomb.remove(bomb)
    
    def screen_update(self):
        self.place_bomb()
        self.check_collision()
        self.check_bottom()
    
    def check_lifes(self):
        if self.lifes <= 0:
            self.print_text(self.font_b,480,400,"Game over",(255,0,0))
            return 0
        if self.lifes >=1:
            return 1   
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill((0,0,0))
            #main def
            self.print_text(self.font_s,0,0,"LIVES:"+str(self.lifes),(255,255,255))
            self.print_text(self.font_s,800,0,"SCORE:"+str(self.scores),(255,255,255))
            if self.check_lifes():
                self.rec.move_rec()
                self.screen_update()
                self.Bomb.update()
            self.clock.tick(60)
            pygame.display.update()
    
if __name__ == '__main__':
    ai = Bomb_catcher()
    ai.run_game()
            