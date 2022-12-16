from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD
import random

class Cloud:

    X_POS =  SCREEN_WIDTH 
    
    def __init__(self):
        self.image = CLOUD
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS 
        self.rect.y = random.randint(50, 100)
        self.width = self.image.get_width()

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -self.width:
            self.rect.x = self.X_POS
            self.rect.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
