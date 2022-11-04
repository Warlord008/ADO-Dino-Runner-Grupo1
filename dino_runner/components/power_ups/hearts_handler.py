import pygame
from dino_runner.components.power_ups.hearts import Heart


class heartmanager():
    def __init__(self, lives):
        self.heart_count = lives

    def draw(self, screen):
        x_position = 10
        y_position = 20

        for counter in range(self.heart_count):
            if self.heart_count > 0:
                heart = Heart(x_position, y_position)
                heart.draw(screen)
                x_position += 40
            else:
                self.heart_count += 5
                
    def reduce_heart_count(self):
        self.heart_count -= 1


