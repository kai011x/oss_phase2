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
    #=====글로벌 변수 선언=====#
    global Display_surface, clock, player, bullet
    
    #=====파이게임 초기화=====#
    pygame.init()
    
    #=====디스플레이 크기 설정=====#
    Display_surface = pygame.display.set_mode((Display_width,Display_height))

    #=====디스플레이 이름 설정=====#
    pygame.display.set_caption("2023312005's game")
    
    #=====틱 설정=====#
    clock = pygame.time.Clock()

def run_Game():
    #=====글로벌 변수 선언=====#
    global Display_surface, clock, player,player_size, bullet
    
    #=====플레이어 크기=====#
    player_size = 10
    
    #=====플레이어 위치 초기 설정(중앙)=====#
    x = Display_width*0.5
    y = Display_height*0.5
    
    #=====플레이어 초기 방향(우측)=====#
    direction = RIGHT
    
    #=====플레이어 이동 속도 초기 설정=====#
    move_speed =0.5
    
    #=====플레이어 이동 수치 초기 설정=====#
    move_x = 0
    move_y = 0
    
    #=====총알 좌표&속도=====#
    bulletXYD = []
    bulletspeed = 15
        
    #=====게임 시작 식별자 초기화(초기 = True)=====#
    Isrun = True
    while Isrun:
        
        #=====게임틱 저장(60프레임)=====#
        FPS = clock.tick(60)
        
        #=====이벤트 입력 식별=====#
        for event in pygame.event.get():
            
            #=====게임 창 종료=====#
            if event.type == QUIT:
                terminate()
                Isrun = False
            #=====플레이어 행동 식별=====#
            if event.type == KEYDOWN:
                
                #=====플레이어 이동=====#
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
                    
                #=====총알 발사(발사 위치 저장)=====#
                elif event.key == pygame.K_SPACE:
                    bulletX = x
                    bulletY = y
                    bulletXYD.append([bulletX,bulletY,direction])
                    
                #=====게임 종료=====#
                if event.key == K_ESCAPE:
                    terminate()
                    Isrun = False
                    
            #=====미행동 판별=====#
            if event.type in [pygame.KEYUP]:
                if event.key == K_a or event.key == K_d:
                    move_x = 0
                elif event.key == K_s or event.key == K_w:
                    move_y = 0
            
                
        #=====플레이어&배경 업데이트=====#        
        Display_surface.fill(BLACK)
        drawplayer(x,y)
        
        #=====총알 경로 그리기=====#
        if len(bulletXYD) != 0:
            for i,bxy in enumerate(bulletXYD):
                if bulletXYD[i][2]==RIGHT:
                    bxy[0] += bulletspeed
                    bulletXYD[i][0] = bxy[0]
                    if bxy[0] >= Display_width:
                        try:
                            bulletXYD.remove(bxy)
                        except:
                            pass
                elif bulletXYD[i][2]==LEFT:
                    bxy[0] -= bulletspeed
                    bulletXYD[i][0] = bxy[0]
                    if bxy[0] <= 0:
                        try:
                            bulletXYD.remove(bxy)
                        except:
                            pass
                elif bulletXYD[i][2]==UP:
                    bxy[1] -= bulletspeed
                    bulletXYD[i][1] = bxy[1]
                    if bxy[1] <= 0:
                        try:
                            bulletXYD.remove(bxy)
                        except:
                            pass
                elif bulletXYD[i][2]==DOWN:
                    bxy[1] += bulletspeed
                    bulletXYD[i][1] = bxy[1]
                    if bxy[1] >= Display_height:
                        try:
                            bulletXYD.remove(bxy)
                        except:
                            pass
                        
        if len(bulletXYD) != 0:
            for bxy in bulletXYD:
                #bulletrect = pygame.rect(bx,by,player_size/2,player_size/2)
                pygame.draw.circle(Display_surface,BLUE,(bxy[0],bxy[1]),5,5)
                
        #=====플레이어 이동 위치 조정=====#
        x += move_x*FPS
        y += move_y*FPS
        
        #=====Display 이탈 제한=====#
        if x-player_size <= 0:
            x = player_size
        elif x > Display_width - player_size:
            x = Display_width - player_size
        
        if y-player_size <= 0:
            y = player_size
        elif y > Display_height - player_size:
            y = Display_height - player_size
            
        #===========================================#
        
        pygame.display.update()
    
    pygame.quit()

#=====게임 종료 함수=====#
def terminate():
    pygame.quit()
    sys.exit()

#=====플레이어 오브젝트 생성=====#
def drawplayer(x,y):
    pygame.draw.circle(Display_surface,WHITE,(x,y),player_size,10)


#=====게임 초기화&게임 실행=====#
init_Game()
run_Game()