
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Bird

from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD

import pygame
import random
    
OBSTACLES = [Bird(BIRD), Cactus(LARGE_CACTUS), Cactus(SMALL_CACTUS)]
class Obstacle_handler():

    def __init__(self):
        self.obstacles = []

    def update (self, speed, dino):
        if len(self.obstacles) == 0:
            number = random.randint(1,3)
            if number == 1: self.obstacles.append(Bird(BIRD))
            elif number == 2: self.obstacles.append(Cactus(LARGE_CACTUS))
            elif number == 3: self.obstacles.append(Cactus(SMALL_CACTUS))

            #self.obstacles.append(Bird(BIRD))
            #self.obstacles.append(Cactus(LARGE_CACTUS))
            #self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(speed)

            if obstacle.image_rect.colliderect(dino.image_rect): ## dino.image_rect
                pygame.time.delay(10)
                self.obstacles.clear()

            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.clear()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
