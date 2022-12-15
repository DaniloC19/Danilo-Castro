import pygame
from dino_runner.utils.constants import FONT_STYLE
class Score: 
    def __init__(self):
        self.highest_score = []
        self.score = 0 

    def update_score(self, game_speed):
        self.score += 1
        
        if self.score % 200 == 0 and game_speed < 500:
            game_speed += 5 

    def draw_score(self, screen):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score {self.score}', True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        screen.blit(text, text_rect)

    def hignest_scores(self, death_counter):
        # flag = True
        if death_counter > 0: 
            self.highest_score.append(self.score)
        # while flag:
        #     flag = False
        #     for i in range(len(self.highest_score) - 1):
        #         if self.highest_score[i] > self.highest_score[i + 1]:
        #             self.highest_score[i], self.highest_score[i + 1] = self.highest_score[i + 1], self.highest_score[i]
        #             flag = True                   
        self.highest_score.sort()
        return self.highest_score[len(self.highest_score) - 1]
        