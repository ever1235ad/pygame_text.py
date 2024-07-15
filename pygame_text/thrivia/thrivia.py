import pygame
import sys
from show_question import Show_question
class Thrivia():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,800))
        self.screen.fill((0,0,0))
        self.state = 1
        self.show_q = Show_question(self)
        pygame.display.set_caption("Thrivia Game")
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.show_q.show_still_font()
            self.show_q.show_score()
            self.show_q.read_txt()
            self.show_q.show_txt()
            self.show_q.show_answer()
            pygame.display.update()
            
if __name__ == '__main__':
    game = Thrivia()
    game.run_game()