class Settings:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800       #在主py文件中改
        self.bg_color=(150,150,150)
        
        self.ship_limit = 3
        
        self.alien_points = 50
        
        self.bullet_width= 1000
        self.bullet_height= 15  #在bullet中改
        self.bullet_color=(0,255,0)
     
        self.fleet_drop_speed = 10.0
        
        self.speedup_scale = 1.1
        self.score_scale =1.5
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.fleet_direction = 1
        self.alien_speed = 3.0
        self.bullet_speed=10.0
        self.ship_speed = 5.0
        
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)
    