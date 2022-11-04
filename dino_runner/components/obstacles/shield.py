from dino_runner.components.obstacles.obstacles import Obstacle
import random

class Shield(Obstacle):
    def __init__(self, images):
        index = 0
        super().__init__(images, index)
        self.image_rect.y = random.randint(100,300)