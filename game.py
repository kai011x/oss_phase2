import random, sys, time
import pygame

Display_width = 600
Display_height = 300

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def init_Game():
    global Display_surface, clock
    pygame.init()
    Display_surface = pygame.display.set_mode((Display_width,Display_height))
    pygame.display.set_caption("2023312005's game")
    clock = pygame.time.Clock()


pygame.quit()
