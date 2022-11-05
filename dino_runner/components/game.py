import pygame
from dino_runner.components.obstacles.obstacle_handler import Obstacle_handler
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.clouds import Cloud
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DINOSAUR_SCORE, DEAD, PLAY, MAX_LIVES,PRE_LEVEL_MUSIC,BACKGROUND_MUSIC,GAME_OVER_SOUND,SPECIAL_FONT, MOON_IMAGE, SUN_IMAGE
from dino_runner.utils.text_utils import BLACK_RGB, WHITE_RGB
from dino_runner.utils import text_utils

pygame.init()

from dino_runner.components.power_ups.hearts_handler import heartmanager

from pygame import mixer
mixer.init()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(DINOSAUR_SCORE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.dinosaur = Dinosaur()
        self.cloud = Cloud()
        self.obstacle_handler = Obstacle_handler()
        self.playing = False
        self.running = True
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 1
        self.points_record = 100
        self.score_time = 400
        self.lives = 5
        self.game_over_sound_times = 1
        self.dead_image = DEAD
        self.night_mode = False

        self.player_heart_manager = heartmanager(self.lives)

    def reset_attibute(self):
        self.playing = True
        self.dinosaur = Dinosaur()
        self.obstacle_handler = Obstacle_handler()
        self.lives = 5
        self.points = 1
        self.game_over_sound_times = 1
        self.game_speed = 20
        self.night_mode = False

    def execute(self):
        while self.running:
            if not self.playing:
                mixer.music.stop()
                self.show_menu()

    def run(self):
        # Game loop: events - update - draw
        self.reset_attibute()
        times = 1
        while self.playing:
            if times == 1:
                mixer.music.play(-1)
                times -= 1
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = True
                self.execute()

    def update(self):
        dino_event = pygame.key.get_pressed()
        self.obstacle_handler.update(self)
        self.dinosaur.update(dino_event)
        self.cloud.update()
        self.update_score()

        if self.lives == 0:
            self.playing = False
            self.running = True
            self.execute()

    def draw(self):
        self.clock.tick(FPS)

        if not self.night_mode: 
            self.screen.fill((255, 255, 255))
            self.screen.blit(SUN_IMAGE, (SCREEN_WIDTH - 100, 100))
        else: 
            self.screen.fill((56, 44, 59))
            self.screen.blit(MOON_IMAGE, (SCREEN_WIDTH - 100, 100))

        self.draw_background()
        self.cloud.draw(self.screen)
        self.dinosaur.draw(self.screen)
        self.obstacle_handler.draw(self.screen)
        self.draw_score()

        self.player_heart_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):

        self.points += 1
        message = "Points: " + str(self.points)
        if self.night_mode: points_text, points_rect = text_utils.get_text_element(message, SCREEN_WIDTH-75, 50, font_color= (255,255,255))
        else: points_text, points_rect = text_utils.get_text_element(message, SCREEN_WIDTH-75, 50)
        self.screen.blit(points_text, points_rect)
        if  (self.points >= self.points_record) and (self.points <= self.points_record + 50):
            message = "¡¡" + str(self.points_record)+ "!!"
            points_text, points_rect = text_utils.get_text_element(message, SCREEN_WIDTH//2, 50)
            self.screen.blit(points_text, points_rect)
            self.screen.blit(DINOSAUR_SCORE, ((SCREEN_WIDTH//2)-70, 30))
        if self.points > self.points_record + 50:
            self.points_record += 500 

    def update_score(self):
        if self.points % 100 ==0:
            self.game_speed += 1 
        if self.points % 300 == 0:
            self.night_mode = True
        elif self.points % 800 == 0:
            self.night_mode = False

    def show_menu(self):

        self.running = True
        black_color = BLACK_RGB
        self.screen.fill(black_color)
        self.show_menu_options()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                pygame.display.quit()
                pygame.quit()
                exit()  

            if event.type == pygame.KEYDOWN:
                PRE_LEVEL_MUSIC.stop()
                self.run()

    def show_menu_options(self):
        if self.points > 1: 
            text, text_rect = text_utils.get_text_element("GAME OVER", font_size= 40, font_color= (255,255,255), font_style= SPECIAL_FONT) 
            points, points_rect = text_utils.get_text_element("Your score was: "+str(self.points), pos_y= (SCREEN_HEIGHT//2) + 40,font_size= 40, font_color= (255,255,255), font_style= SPECIAL_FONT) 
            self.screen.blit(points, points_rect)
            self.screen.blit(self.dead_image, (text_rect.x+ 70, text_rect.y - 120))
            if self.game_over_sound_times == 1:
                GAME_OVER_SOUND.play()
                pygame.time.delay(1500)
                PRE_LEVEL_MUSIC.play()
                self.game_over_sound_times -= 1
        else: 
            text, text_rect = text_utils.get_text_element("Press any key to start", font_size= 40, font_color= (255,255,255), font_style= SPECIAL_FONT)
            self.screen.blit(PLAY, (SCREEN_WIDTH//2 -25, text_rect.y - 100))
            if self.game_over_sound_times == 1:
                PRE_LEVEL_MUSIC.play()
                self.game_over_sound_times -= 1
        self.screen.blit(text, text_rect)
    


