import pygame
FONT_STYLE = 'freesansbold.ttf'
BLACK_RGB = (0,0,0)
WHITE_RGB = (255,255,255)
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

def get_text_element(message, pos_x= SCREEN_WIDTH//2, pos_y= SCREEN_HEIGHT//2, font_size = 20, font_color= BLACK_RGB):
    font = pygame.font.Font(FONT_STYLE, font_size)
    text = font.render(message, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = (pos_x, pos_y)
    return text, text_rect