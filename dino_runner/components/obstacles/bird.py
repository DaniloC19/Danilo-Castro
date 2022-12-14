from pygame.sprite import Sprite
from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle

import random
class Bird(Obstacle):
    
    Y_POS1 = 220
    Y_POS2 = 290
    Y_POS3 = 330
    def __init__(self): 
        self.step_index = 10
         # self.rect = self.image.get_rect()
        self.height = random.randint(0,2)
        self.frame = random.randint(0,1)
# [0] if self.step_index < 5 else BIRD[1]
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        super().__init__(self.image)
      
        if self.step_index >= 10:
                self.step_index = 0
        
        if self.height == 0:
            self.rect.y = self.Y_POS2    
        elif self.height == 1:
            self.rect.y = self.Y_POS2
        elif self.height == 2:
            self.rect.y = self.Y_POS3

    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.step_index += 1

    def fly_animation(self):
        self.fly()

        if self.step_index >= 10:
            self.step_index = 0
    
    

        
        
        # self.bird_fly = True

    # def animation(self):
    #     if self.bird_fly:
    #         self.fly()

    #     if self.step_index >=10:
    #         self.step_index = 0 
    
    # def fly(self):
    #     height = random.randint(0,2)
        
    #     self.rect = self.image.get_rect()
        
    #     if height == 0:
    #         self.rect.y = self.Y_POS1
    #     elif height == 1:
    #         self.rect.y = self.Y_POS2
    #     elif height == 2:
    #         self.rect.y =self.Y_POS3
        

    # def draw(self, screen): 
    #     screen.blit(self.image, (self.rect.x, self.rect.y))

