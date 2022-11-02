
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Bird

from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD

import pygame
import random

class Obstacle_handler():
    ##ALLOWED_OBSTACLES = [ Cactus(SMALL_CACTUS), Cactus(LARGE_CACTUS), Bird(BIRD)] ##

    def __init__(self):
        self.obstacles = []

    def update (self, speed, dino):
        if len(self.obstacles) == 0:
            ##self.obstacles.append( self.ALLOWED_OBSTACLES[random.randint(0,1)] ) ##
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(speed)

            if dino.image_rect.colliderect(obstacle.image_rect): ##
                print("1")
                pygame.time.delay(100)
                self.obstacles.pop()

            if obstacle.image_rect.x < -obstacle.image_rect.width:
                print("2")
                self.obstacles.pop()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
