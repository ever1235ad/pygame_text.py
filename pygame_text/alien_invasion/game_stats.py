class GameStats:
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.game_active = False
        self.reset_stats()
        self.score = 0
        self.level = 1
        with open('high_score.txt','r') as file:
            self.high_score = int(file.read())
                
        
    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1