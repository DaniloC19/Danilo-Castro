import pygame
import random

import os
from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE,SMALL_CACTUS
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

from dino_runner.utils.constants import DINO_DEAD


from dino_runner.components.dinosaur import Dinosaur
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "..","assets")



class ObstacleManager:
  def __init__(self):
    self.dino = Dinosaur()
    self.obstacles = []
    pygame.mixer.music.load(os.path.join(IMG_DIR, "Other/sfx.mp3"))
    
  def generate_obstacle(self, obstacle_type):
    if obstacle_type == 0:
      cactus_type = 'SMALL'
      obstacle = Cactus(cactus_type)
    elif obstacle_type == 1:
      cactus_type = 'LARGE'
      obstacle = Cactus(cactus_type)
    else:
      obstacle = Bird()
    return obstacle
    
  def update(self, game):
    if len(self.obstacles) == 0:
      obstacle_type = random.randint(0, 2)
      obstacle = self.generate_obstacle(obstacle_type)
      self.obstacles.append(obstacle)
      
    for obstacle in self.obstacles:
      obstacle.update(game.game_speed, self.obstacles)
      if game.player.dino_rect.colliderect(obstacle.rect):

        if game.player.type == SHIELD_TYPE:
          pass
        elif game.player.type == HAMMER_TYPE:  
          self.obstacles.pop()
        else:
          
          pygame.mixer.music.play()
          self.dino.image = DINO_DEAD
          game.death_count.count += 1
          pygame.time.delay(1000)
          game.playing = False
          break
           
          
  
  def draw(self, screen):
    for obstacle in self.obstacles:
      obstacle.draw(screen)
      
  def reset_obstacles(self):
    self.obstacles = []