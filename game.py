import random
import sys
import time
import pygame

Display_width = 900
Display_height = 600

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
    global Display_surface, clock, player
    pygame.init()
    Display_surface = pygame.display.set_mode((Display_width,Display_height))
    pygame.display.set_caption("2023312005's game")
    clock = pygame.time.Clock()

def run_Game():
    global Display_surface, clock, player,player_size 
    
    #플레이어 크기
    player_size = 10
    
    #플레이어 초기 위치
    x = Display_width*0.5
    y = Display_height*0.5
    
    Isrun = True
    while Isrun:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
                
                
        Display_surface.fill(BLACK)
        drawplayer(x,y)
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()


def drawplayer(x,y):
    pygame.draw.circle(Display_surface,WHITE,(x,y),player_size,10)

init_Game()
run_Game()