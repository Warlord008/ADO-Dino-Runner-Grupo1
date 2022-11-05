import pygame
import os
from pygame import mixer
mixer.init()

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

DEAD = pygame.image.load("ADO-Dino-Runner-Grupo1/dino_runner/assets/Dino/DinoDead.png")

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DINOSAUR_SCORE = pygame.image.load(os.path.join(IMG_DIR, 'Other/dinosaurs_score.png'))

DEFAULT_TYPE = "default"

PLAY = pygame.image.load(os.path.join(IMG_DIR, 'Other/play.png'))

MAX_LIVES = 3
BACKGROUND_MUSIC = mixer.music.load('ADO-Dino-Runner-Grupo1/dino_runner/assets/Music/03.wav')
mixer.music.set_volume(0.2)
PRE_LEVEL_MUSIC = mixer.Sound('ADO-Dino-Runner-Grupo1/dino_runner/assets/Music/level.wav')
PRE_LEVEL_MUSIC.set_volume(0.2)
GAME_OVER_SOUND = mixer.Sound('ADO-Dino-Runner-Grupo1/dino_runner/assets/Music/ominous.wav')
GAME_OVER_SOUND.set_volume(0.2)

SPECIAL_FONT  = 'ADO-Dino-Runner-Grupo1/dino_runner/assets/Other/Font/airstrike.ttf'

DAMAGE_SOUND = mixer.Sound('ADO-Dino-Runner-Grupo1/dino_runner/assets/Music/damage.wav')
DAMAGE_SOUND.set_volume(0.2)
BOOST_SOUND = mixer.Sound('ADO-Dino-Runner-Grupo1/dino_runner/assets/Music/boost.wav')
BOOST_SOUND.set_volume(0.2)
SHILED_DAMAGE = mixer.Sound('ADO-Dino-Runner-Grupo1/dino_runner/assets/Music/shiledroze.wav')
SHILED_DAMAGE.set_volume(0.2)

SUN_IMAGE = pygame.image.load(os.path.join(IMG_DIR, 'Other/sun.png'))
MOON_IMAGE = pygame.image.load(os.path.join(IMG_DIR, 'Other/night.png'))