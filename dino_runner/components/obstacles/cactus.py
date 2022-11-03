from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS
import random

class Cactus(Obstacle):
    def __init__(self, images):
        index = random.randint(0,2)
        super().__init__(images, index)
        if images == SMALL_CACTUS: self.image_rect.y = 320 
        else: self.image_rect.y = 300

    
