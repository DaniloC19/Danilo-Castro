from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
import random
class Cactus(Obstacle):
    def __init__(self):
        self.cactus_size = random.randint(0,1)
        self.size = [SMALL_CACTUS, LARGE_CACTUS]
        self.type = random.randint(0,2)
        super().__init__(self.size[self.cactus_size][self.type])
        self.rect.y = 325

    # def cactus_type(self):
    #     if self.cactus_size == 0:
    #         super().__init__(SMALL_CACTUS, self.type)
            

    #     elif self.cactus_size == 1:
    #         super().__init__(LARGE_CACTUS, self.type)
    #         self.rect.y = 325
          
