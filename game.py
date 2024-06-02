import random
import sys
import time
import pygame
from pygame.locals import *
import datetime

#=====게임 설정=====#
Display_width = 900
Display_height = 600
FPS = 0

#=====색상 정의=====#
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#=====키 변수 설정=====#
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


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
    global Display_surface, clock, player,player_size, bullet, Isrun
    
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
    
    #=====적 오브젝트 설정=====#
    enemy_speed = 3
    enemy_list = []
    enemy_limit = 1
    enemy_count = 0
    enemy_size = 10
    direction_list = [LEFT,RIGHT,UP,DOWN]
    
    #=====시작 시간 설정=====#
    start_time = datetime.datetime.now()
    
        
    #=====게임 시작 식별자 초기화(초기 = True)=====#
    Isrun = True
    while Isrun:
        
        #=====게임틱 저장(60프레임)=====#
        FPS = clock.tick(60)
        
        #=====적 생성=====#
        if enemy_count < enemy_limit:
            random_direction = random.randrange(0,4)
            if(random_direction==0):
                enemy_x = Display_width
                enemy_y = random.randrange(10,Display_height)
                enemy_list.append([enemy_x,enemy_y,direction_list[random_direction]])
                enemy_count+=1
            elif(random_direction==1):
                enemy_x = 0
                enemy_y = random.randrange(10,Display_height)
                enemy_list.append([enemy_x,enemy_y,direction_list[random_direction]])
                enemy_count+=1
            elif(random_direction==2):
                enemy_x = random.randrange(10,Display_width)
                enemy_y = Display_height
                enemy_list.append([enemy_x,enemy_y,direction_list[random_direction]])
                enemy_count+=1
            elif(random_direction==3):
                enemy_x = random.randrange(10,Display_width)
                enemy_y = 0
                enemy_list.append([enemy_x,enemy_y,direction_list[random_direction]])
                enemy_count+=1
            
        
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
            
        #=====시간 변화 인식=====#
        cur_time = datetime.datetime.now()
        delta_time = round((cur_time - start_time).total_seconds())
                
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
                pygame.draw.circle(Display_surface,BLUE,(bxy[0],bxy[1]),5,5)
                
        #=====적 이동 경로 그리기=====#
        if len(enemy_list) != 0:
            for i,exy in enumerate(enemy_list):
                if enemy_list[i][2]==RIGHT:
                    exy[0] += enemy_speed
                    enemy_list[i][0] = exy[0]
                    if exy[0] >= Display_width:
                        try:
                            enemy_list.remove(exy)
                            enemy_count-=1
                        except:
                            pass
                elif enemy_list[i][2]==LEFT:
                    exy[0] -= enemy_speed
                    enemy_list[i][0] = exy[0]
                    if exy[0] <= 0:
                        try:
                            enemy_list.remove(exy)
                            enemy_count-=1
                        except:
                            pass
                elif enemy_list[i][2]==UP:
                    exy[1] -= enemy_speed
                    enemy_list[i][1] = exy[1]
                    if exy[1] <= 0:
                        try:
                            enemy_list.remove(exy)
                            enemy_count-=1
                        except:
                            pass
                elif enemy_list[i][2]==DOWN:
                    exy[1] += enemy_speed
                    enemy_list[i][1] = exy[1]
                    if exy[1] >= Display_height:
                        try:
                            enemy_list.remove(exy)
                            enemy_count-=1
                        except:
                            pass
                        
        if len(enemy_list) != 0:
            for exy in enemy_list:
                #bulletrect = pygame.rect(bx,by,player_size/2,player_size/2)
                pygame.draw.circle(Display_surface,RED,(exy[0],exy[1]),10,10)
                
                
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
            
        #=====충돌 확인=====#
        if len(enemy_list) != 0:
            for exy in enemy_list:
                if p_e_crach_check(x,y,exy[0],exy[1]):
                    gameOver()
        
        if (len(enemy_list) != 0) and (len(bulletXYD) != 0 ):
            for exy in enemy_list:
                for bxy in bulletXYD:
                    if b_e_crash_check:
                        enemy_list.remove(exy)
                        bulletXYD.remove(bxy)
      
        #=====시간 출력=====#
        print_time(delta_time)
        
        
        pygame.display.update()
    
    pygame.quit()

#=====게임 종료 함수=====#
def terminate():
    pygame.quit()
    sys.exit()

#=====충돌 감지 함수=====#
def b_e_crash_check(bx,by,ex,ey): #: bullet - enemy 충돌 check
    x_gap = abs(bx-ex)
    y_gap = abs(by-ey)
    if x_gap < 5 and y_gap < 5:
        return True
    else:
        return False
    

def p_e_crach_check(px,py,ex,ey): #: player - enemy 충돌 check
    x_gap = abs(px-ex)
    y_gap = abs(py-ey)
    if x_gap < player_size+5 and y_gap < player_size+5:
        return True
    else:
        return False
    
#=====플레이어 오브젝트 생성 함수=====#
def drawplayer(x,y):
    pygame.draw.circle(Display_surface,WHITE,(x,y),player_size,10)

#=====게임 오버 함수=====#
def gameOver():
    global Display_surface, Isrun
    gofont = pygame.font.SysFont(None,100)
    gotext = gofont.render('GAME OVER',True,WHITE) #go = gameover
    gotextpos = gotext.get_rect()
    gotextpos.center = (Display_width/2,Display_height/2-30)
    Display_surface.blit(gotext,gotextpos)
    
    rsfont = pygame.font.SysFont(None,60)
    rstext = rsfont.render('Press R to restrart',True,WHITE)
    rstextpos = rstext.get_rect()
    rstextpos.center = (Display_width/2,Display_height/2+30)
    Display_surface.blit(rstext,rstextpos)
    
    pygame.display.update()
    
    Gameover = True
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                Isrun = False
            elif event.type == KEYDOWN:
                if event.key == K_r:
                    run_Game()
                elif event.key == K_ESCAPE:
                    terminate()
                    Isrun = False

#=====시간 출력 함수=====#
def print_time(delta_time):
    tmfont = pygame.font.SysFont(None,40) #tm = time
    tmtext = tmfont.render("Time : {}".format(delta_time),True,WHITE) #go = gameover
    tmtextpos = tmtext.get_rect()
    tmtextpos.center = (65,25)
    Display_surface.blit(tmtext,tmtextpos)

#=====게임 초기화&게임 실행=====#
init_Game()
run_Game()