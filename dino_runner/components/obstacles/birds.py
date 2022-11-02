from dino_runner.components.obstacles.obstacles import Obstacle
import random
class Bird(Obstacle):
    def __init__(self, images):
        index = random.randint(0,1)
        super().__init__(images, index)
        self.image_rect.y = random.randint(100,300)
