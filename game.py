import random
import sys
import time
import pygame
from pygame.locals import *

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

FPS = 0

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
    
    #플레이어 초기 방향
    direction = RIGHT
    
    #플레이어 이동 속도
    move_speed =0.5
    
    #플레이어 이동 수치
    move_x = 0
    move_y = 0
    
    Isrun = True
    while Isrun:
        FPS = clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                Isrun = False
            
            if event.type == KEYDOWN:
                if event.key == pygame.K_a:
                    direction = LEFT
                    move_x -= move_speed
                elif event.key == pygame.K_d:
                    direction = RIGHT
                    move_x += move_speed
                elif event.key == pygame.K_w:
                    direction = UP
                    move_y -= move_speed
                elif event.key == pygame.K_s:
                    direction = DOWN
                    move_y += move_speed
                if event.key == K_ESCAPE:
                    terminate()
                    Isrun = False
                    
            if event.type in [pygame.KEYUP]:
                if event.key == K_a or event.key == K_d:
                    move_x = 0
                elif event.key == K_s or event.key == K_w:
                    move_y = 0
                    
                
                
        Display_surface.fill(BLACK)
        drawplayer(x,y)
        
        x += move_x*FPS
        y += move_y*FPS
        
        pygame.display.update()
    
    pygame.quit()

def terminate():
    pygame.quit()
    sys.exit()

def drawplayer(x,y):
    pygame.draw.circle(Display_surface,WHITE,(x,y),player_size,10)

init_Game()
run_Game()