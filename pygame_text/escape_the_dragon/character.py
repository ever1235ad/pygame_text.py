import pygame
class Character(pygame.sprite.Sprite):
    def __init__(self,ai_game,framerate):
        super().__init__()
        self.clock = pygame.time.Clock()
        self.screen = ai_game.screen
        self.game_active = ai_game.game_active
        self.dra = ai_game.dragon
        self.framerate = framerate
        self.frame = 0
        self.last_time = 0
        self.image = pygame.image.load("data_image/character.png")
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        self.column = 0
        self.frame_width = self.image_width // 14
        self.frame_height = self.image_height
        self.x = 500
        self.y = 590
        self.rect = (self.x,self.y,self.frame_width,self.frame_height)
        self.a = 0
        self.v_y = 0
        
    def update(self):
        self.check_jump()
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.last_time >= self.framerate:
            self.frame_img_rect = pygame.Rect(self.frame_width * self.column,0,self.frame_width,self.frame_height)
            self.frame_img = self.image.subsurface(self.frame_img_rect) 
            self.screen.blit(self.frame_img,(self.x,self.y))  #character_pos
            self.last_time = self.current_time
            self.column += 1     
            if self.column > 13:
                self.column = 0
        
    def check_jump(self):
        if self.y <= 590:
            if self.v_y == 0:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_k:
                            self.v_y = -16.0
                            self.a = 0.6
                        elif event.key == pygame.K_j:
                            self.v_y = -15.0
                            self.a = 0.6
                        elif event.key == pygame.K_l:
                            self.v_y = -15.0
                            self.a = 0.6
                        elif event.key == pygame.K_i:
                            self.game_active = False
                            self.dra.x = -1000
        self.y += self.v_y
        self.v_y += self.a
        if self.y > 590:
            self.v_y = 0   
            self.y = 590