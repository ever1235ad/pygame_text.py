import pygame
import sys
import time
import threading
from dragon import Dragon
from character import Character
from fireball import Fireball
import pygame.image
class Escape_the_dragon():
    def __init__(self):
        pygame.init()
        self.data_init()
        self.group = pygame.sprite.Group()
        self.font = pygame.font.Font(None,18)
        self.font_s = pygame.font.Font(None,30)
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.scr_width,self.scr_height))
        self.dragon =  Dragon(self,self.dra_framerate)
        self.character = Character(self,self.cha_framerate)
        self.fireball = Fireball(self,self.fir_framerate)
        self.cha_sound = pygame.mixer.Sound('character_injury.mp3')
        self.dra_sound = pygame.mixer.Sound('dragon_injury.mp3')
        
        
        '''self.sprite_dra = pygame.sprite.Sprite()
        self.sprite_cha = pygame.sprite.Sprite()JKLKLK
        self.sprite_cha.rect = self.character.rect
        self.sprite_dra.rect = self.dragon.rect
        self.group.add(self.sprite_dra)
        self.group.add(self.sprite_cha)'''
        pygame.display.set_caption("Escape the dragon")
        
    def print_text(self,font,text,color,pos):
        imgText = font.render(text,True,color)
        self.screen.blit(imgText,pos)
        
    def sprite_collide(self):
        #collision = pygame.sprite.collide_rect(self.sprite_cha,self.sprite_dra)
        #if collision:
        if self.game_active:
            self.print_text(self.font,"Press 'j' 'k' 'l' to jump",(255,255,255),(self.scr_width // 2 -50,self.scr_height / 4))
        if self.check_collide_1():
            self.game_active = False
            self.print_text(self.font,"G A M E  O V E R!",(255,255,255),(450,400))
            pygame.mixer.music.stop()
        if self.check_collide_3():
            self.dragon.x -= 40
            self.score += 100
            self.dra_sound.play()
            self.print_text(self.font,"+100",(255,255,255),(self.dragon.x + 150,self.dragon.y - 30))
        if self.check_collide_2():
            self.character.x -= 20
            self.cha_sound.play()
        if self.dragon.x + self.dragon.r_img_width <= 0:
            self.game_active = False
            self.print_text(self.font,"THE   MONSTER   HAS   BEEN   DEFEATED !",(255,255,255),(self.scr_width // 2 - 120,self.scr_height / 4))
            self.print_text(self.font,"Y O U   W I N!",(255,255,255),(450,400))

    def check_collide_1(self):
        if self.dragon.x + self.dragon.r_img_width - 45 >= self.character.x :
            return True
        
    def check_collide_2(self):
        if self.fireball.x + 30 <= self.character.x + self.character.frame_width and self.fireball.x >= self.character.x + 30:
            if self.fireball.y - self.character.frame_height <= self.character.y:
                self.fireball.x = self.scr_width + 20
                return True
        
    def check_collide_3(self):
        if self.fireball.x <= self.dragon.x + self.dragon.r_img_width - 10:
            self.fireball.x = self.scr_width + 20
            return True
        
    def digit_high_check_load(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            self.file = open("escape_the_dragon_score.txt","w")
            self.file.write(str(self.high_score))
            self.file.close()
        self.print_text(self.font_s,f"High Score:{str(self.high_score)}",(255,255,255),(self.scr_width //2 - 40,20))
    
    def data_init(self):
        self.game_active = True
        self.score = 0
        self.dra_framerate = 100
        self.fir_framerate = 10
        self.cha_framerate = 1
        self.scr_width = 1000
        self.scr_height = 800
        self.bg1_x = 0
        self.bg2_x = self.scr_width // 2
        self.bg3_x = self.scr_width
        self.music = pygame.mixer.music.load('Megalovania.mp3')
        pygame.mixer.music.play(-1)
        self.file = open("escape_the_dragon_score.txt","r")
        self.high_score = int(self.file.readline())
        self.file.close()
        
    def bg_load(self):
        bg_image = pygame.image.load("data_image/bg.png")
        scaled_bg = pygame.transform.smoothscale(bg_image,(self.scr_width // 2, self.scr_height // 2))
        self.screen.blit(scaled_bg,(self.bg1_x,self.scr_height // 2))
        self.screen.blit(scaled_bg,(self.bg2_x,self.scr_height // 2))
        self.screen.blit(scaled_bg,(self.bg3_x,self.scr_height // 2))
        self.bg1_x -= 2
        self.bg2_x -= 2
        self.bg3_x -= 2
        scaled_bg_width = scaled_bg.get_width()
        if self.bg1_x <= - scaled_bg_width:
            self.bg1_x = self.scr_width
        if self.bg2_x <= - scaled_bg_width:
            self.bg2_x = self.scr_width
        if self.bg3_x <= - scaled_bg_width:
            self.bg3_x = self.scr_width
        self.print_text(self.font_s,f"SCORE:{str(self.score)}",(255,255,255),(self.scr_width - 150,20))
        self.score += 1
        
        #开挂：i键一键通关
        '''for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_i:
                            self.game_active = False
                            self.dragon.x = -1000'''
    
    
    def run_game(self):
        while True:
            for evnet in pygame.event.get():
                if evnet.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill((255,0,0))
            self.sprite_collide()
            if self.game_active:
                self.bg_load()
                self.digit_high_check_load()
                self.dragon.update()
                self.character.update()
                self.fireball.update()
            self.clock.tick(60)
            pygame.display.update()
if __name__ == "__main__":
    ai = Escape_the_dragon()
    ai.data_init()
    ai.run_game()