import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import CLOUD

class Cloud(Sprite):
    def __init__(self):
        self.image = CLOUD
        self.image_rect = self.image.get_rect()
        #number_of_clouds = random.randint(1,3)
        #for i in range(number_of_clouds):
            #self.image_rect_x = random.randint(250,600)
            #self.image_rect_y = random.randint(5,200)
        self.image_rect_x = random.randint(250,600)
        self.image_rect_y = random.randint(5,200)

    def update(self):
        velocity_of_movement = random.randint(2,4)
        #for i in range(number_of_clouds):
            #self.image_rect_x -= velocity_of_movement
        self.image_rect_x -= velocity_of_movement
        if self.image_rect_x < -100:
            self.image_rect_x = 1200
            self.image_rect_y = random.randint(5,200) 

    def draw(self, screen):
        screen.blit(self.image, (self.image_rect_x, self.image_rect_y))
        

