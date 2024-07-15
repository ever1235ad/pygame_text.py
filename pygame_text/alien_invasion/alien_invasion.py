import sys
import pygame
from time import sleep
from game_stats import GameStats
from settings import Settings                     #撞船后船的y不变，x回到中间           J的连点
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard
class AlienInvasion:
    def __init__(self):                             #初始化游戏
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.ship = Ship(self)
        self.bullet = Bullet(self)
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.prep_music_play()
        pygame.display.set_caption("Alien Invasion")
        self.bullets =pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self,"Play")
        self.last_shot_time = pygame.time.get_ticks()

    def _check_events(self):
        for event in pygame.event.get():          #飞船的移动
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type ==pygame.KEYDOWN:         #按下键
                self._check_keydown_events(event)
            if event.type==pygame.KEYUP:          #松开键
                self._check_keyup_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    def _check_play_button(self,mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if not self.stats.game_active and button_clicked:
            self.stats.reset_stats()
            self.settings.initialize_dynamic_settings()
            self.stats.game_active = True
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            #self.ship.center_ship()
            pygame.mixer.music.stop()
            self.main_music_play()
            pygame.mouse.set_visible(False)
    def _check_keydown_events(self,event): 
        if event.key==pygame.K_q:
            sys.exit()
        if event.key==pygame.K_d:
            self.ship.moving_right=True
        if event.key==pygame.K_a:
            self.ship.moving_left=True
        if event.key==pygame.K_w:
            self.ship.moving_up=True
        if event.key==pygame.K_s:
            self.ship.moving_down=True
       
    def _check_fire_bullton(self):
        self.bullet_interval = 100       
        keys =pygame.key.get_pressed()
        if keys[pygame.K_j]:
          self.current_shot_time = pygame.time.get_ticks()
          if self.current_shot_time - self.last_shot_time >= self.bullet_interval:
            self._fire_bullet()
            self.last_shot_time = self.current_shot_time
               
   
    def _check_keyup_events(self,event):
        if event.key==pygame.K_d:
            self.ship.moving_right=False
        if event.key==pygame.K_a:
            self.ship.moving_left=False
        if event.key==pygame.K_w:
            self.ship.moving_up=False
        if event.key==pygame.K_s:
            self.ship.moving_down=False
   
    def _fire_bullet(self):
        new_bullet=Bullet(self)                     #什么情况，怎么赋值给bullet啊！！！！
        self.bullets.add(new_bullet)
        new_bullet=Bullet(self)                     #什么情况，怎么赋值给bullet啊！！！！
        self.bullets.add(new_bullet)
        new_bullet=Bullet(self)                     #什么情况，怎么赋值给bullet啊！！！！
        self.bullets.add(new_bullet)
        new_bullet=Bullet(self)                     #什么情况，怎么赋值给bullet啊！！！！
        self.bullets.add(new_bullet)
        new_bullet=Bullet(self)                     #什么情况，怎么赋值给bullet啊！！！！
        self.bullets.add(new_bullet)
        
    def main_music_play(self):
        pygame.mixer.music.load('Laura Shigihara - Brainiac Maniac.mp3')
        pygame.mixer.music.play(-1)
        
    def prep_music_play(self):
        pygame.mixer.music.load('Laura Shigihara - Faster.mp3')
        pygame.mixer.music.play(-1)

        
    def _update_aliens(self):           #更新外星人状态
        self._check_fleet_edges()
        self.aliens.update()
        self._check_aliens_bottom()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
            print('Ship hits !!!')
        
            
        
        
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
            
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points*len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
                
    def _create_fleet(self):        #创建一个外星人编组
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
        number_rows = available_space_y // (2*alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)
                
    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2*alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2*alien_height * row_number
        self.aliens.add(alien)
        
    def _upgrade_screen(self):                      #背景颜色
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():         #这点是写子弹显形的
            bullet.draw_bullet()  
        self.sb.show_score()
        self.aliens.draw(self.screen)
        self.ship.blitme()
        if not self.stats.game_active:
            self.play_button.draw_button()
        
    def _ship_hit(self):     #飞船撞击外星人响应
        self.stats.ship_left -= 1
        if self.stats.ship_left > 0:   
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.__init__(self)
            #self.ship.center_ship()
            sleep(0.75)
        else:
            self.stats.reset_stats()
            self.sb.__init__(self)
            self.stats.game_active = False
            pygame.mixer.music.stop()
            self.prep_music_play()             #这里吧
            self.ship.__init__(self)
            self.stats.__init__(self)
            # self.ship.center_ship()
            pygame.mouse.set_visible(True)
            
        
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
        
 
    def run_game(self):   
    #游戏主体
       
        while True:
            self._check_events()
            self._check_fire_bullton()
            if self.stats.game_active:
                self._update_aliens()
                self._update_bullets()
                self.ship.update()
                self.bullets.update()
            self._upgrade_screen()
            pygame.display.flip()
            self.clock.tick(60)                     #60帧
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()