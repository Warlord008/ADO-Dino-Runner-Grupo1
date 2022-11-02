from asyncio import constants

from dino_runner.utils.constants import JUMPING
from dino_runner.utils.constants import RUNNING
from dino_runner.utils.constants import DUCKING

import pygame
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    DINO_X_POS = 50
    DINO_Y_POS = 300
    INITIAL_STEP = 0
    MAX_STEP = 10
    ACELERATION = 4
    REDUCE_VELOCITY = 0.9
    INITIAL_VELOCITY = 10



    def __init__(self):
        self.image = RUNNING[0]
        self.image_rect = self.image.get_rect()
        self.image_rect_x = self.DINO_X_POS
        self.image_rect_y = self.DINO_Y_POS
        self.step = self.INITIAL_STEP
        self.dino_jump = False
        self.dino_duck = False
        self.dino_run = True
        self.dino_velocity = self.INITIAL_VELOCITY
    
    def update(self, dino_event):
        if self.dino_jump: self.jump()
        if self.dino_run: self.run()
        if self.dino_duck: self.duck()
        if self.step > self.MAX_STEP : self.step = self.INITIAL_STEP
        if dino_event[pygame.K_UP] and not self.dino_jump: 
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        if dino_event[pygame.K_DOWN] and not self.dino_jump: 
            self.dino_run = False
            self.image_rect_y = 340
            self.dino_duck = True
            self.dino_jump = False

    def run(self):
        self.image = RUNNING[0] if self.step <= 5 else RUNNING[1] 
        self.step += 1
        if self.step > self.MAX_STEP : self.step = self.INITIAL_STEP

    def duck(self):
        if self.step <= 5: self.image = DUCKING[0] 
        else: self.image = DUCKING[1] 
        self.step += 1
        if self.step > self.MAX_STEP : self.step = self.INITIAL_STEP
        self.dino_duck = False
        self.image_rect_y = 300
        self.dino_run = True

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.image_rect_y -= self.dino_velocity * self.ACELERATION
            self.dino_velocity -= self.REDUCE_VELOCITY
        if self.dino_velocity < -self.INITIAL_VELOCITY:
            self.image_rect_y = self.DINO_Y_POS
            self.dino_jump = False
            self.dino_run = True
            self.dino_velocity = self.INITIAL_VELOCITY


    def draw(self, screen):
        screen.blit(self.image, (self.image_rect_x, self.image_rect_y))
