
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Bird
from dino_runner.components.obstacles.shield import Shield
from dino_runner.utils import text_utils


from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SHIELD, DAMAGE_SOUND, BOOST_SOUND, SHILED_DAMAGE

from pygame import mixer
mixer.init()

import pygame
import random


class Obstacle_handler():

    def __init__(self):
        self.obstacles = []
        self.step = 0
        self.number = 0
        self.luck_number = 0
        self.shield = False
        self.sorted = False
        self.hit_times = 3

    def update (self, game):
        if len(self.obstacles) == 0:
            self.number = random.randint(1,4)
            self.luck_number = random.randint(1, 10)

            if (self.number == 4) and (self.luck_number == 10): self.sorted = True

            if self.number == 1: self.obstacles.append(Bird(BIRD))
            elif self.number == 2: self.obstacles.append(Cactus(LARGE_CACTUS))
            elif self.number == 3: self.obstacles.append(Cactus(SMALL_CACTUS))
            elif self.sorted: self.obstacles.append(Shield(SHIELD))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed)

            if self.number == 1:
               obstacle.image = BIRD[0] if self.step <= 5 else BIRD[1]
               self.step += 1
               if self.step > 10 : self.step = 0

            if obstacle.image_rect.colliderect(game.dinosaur.image_rect) and not (self.sorted or self.shield): 
                game.player_heart_manager.reduce_heart_count()
                pygame.time.delay(10)
                self.obstacles.clear()
                DAMAGE_SOUND.play()
                game.lives -= 1
            elif obstacle.image_rect.colliderect(game.dinosaur.image_rect) and  (self.sorted):
                BOOST_SOUND.play()
                self.obstacles.clear()
                self.shield = True

            if obstacle.image_rect.colliderect(game.dinosaur.image_rect) and not (self.sorted) and self.shield:
                self.hit_times -= 1
                self.obstacles.clear()
                SHILED_DAMAGE.play()
                if self.hit_times == 0: 
                    self.shield = False
                    self.hit_times = 3

            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.clear()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
