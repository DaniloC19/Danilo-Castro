import pygame 
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from dino_runner.components.obstacles.bird import Bird
class ObstacleManager(Cactus, Bird):
    def __init__(self):
        self.obstacles = []
        

    def update(self, game):
        
        if len(self.obstacles) == 0:
            enemy = random.randint(0,1)
            if enemy == 0:
                cactus = Cactus()
                self.obstacles.append(cactus)
            elif enemy == 1:
                bird = Bird()
                self.obstacles.append(bird)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles: 
            obstacle.draw(screen)

