
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
        self.step = 0
        self.number = 0

    def update (self, game):
        if len(self.obstacles) == 0:
            self.number = random.randint(1,3)
            if self.number == 1: self.obstacles.append(Bird(BIRD))
            elif self.number == 2: self.obstacles.append(Cactus(LARGE_CACTUS))
            elif self.number == 3: self.obstacles.append(Cactus(SMALL_CACTUS))

            #self.obstacles.append(Bird(BIRD))
            #self.obstacles.append(Cactus(LARGE_CACTUS))
            #self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed)

            if self.number == 1:
               obstacle.image = BIRD[0] if self.step <= 5 else BIRD[1]
               self.step += 1
               if self.step > 10 : self.step = 0

            if obstacle.image_rect.colliderect(game.dinosaur.image_rect): ## dino.image_rect
                pygame.time.delay(10)
                self.obstacles.clear()
                game.lives -= 1

            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.clear()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
