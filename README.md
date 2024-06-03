# Reference
[1] https://github.com/pygame/pygame "pygame"

# 지원 Operating Systems 및 실행 방법

## 지원 Operating Systems
|OS| 지원 여부 |
|-----|--------|
|windows | :o:  |
| Linux  | :o: |
|MacOS  | :x:  |

## 실행 방법
### Windows

1. python3.8.10을 설치한다. (추천 사항. 상위 버전 설치시 pygame 호환 문제 발생 가능성 존재.)
2. swiging을 설치한다
```
1. https://sourceforge.net/projects/swig/files/swigwin/swigwin-3.0.2/swigwin-3.0.2.zip/download 에서 파일 다운로드

2. C:\ 경로에 압축해제

3. 시작 > 시스템 환경변수 > 환경 변수... > 시스템 변수, Path, 편집 > 새로만들기, 편집 C:\swigwin-3.0.2 추가 
```
3. Microsoft Visual c++ Build Tools 설치
```
1. https://visualstudio.microsoft.com/ko/visual-cpp-build-tools/ 에서   Build Tools 다운로드 후 실행

2. Visual Studio Installer가 실행 된 경우 해당 버전의 "수정(Modify)" 클릭

3. Desktop & Mobile 에서 c++ build Tools 체크 표시 이후 설치한다

4. 시스템 재부팅
```
4. powershell 창에서 아래 pip3 library를 설치한다

```
pip3 install pygame
pip3 install pylance
```

5. 재부팅 이후 python3 game.py를 실행하면 게임 창이 뜨면서 실행된다.

### Linux
1. 본인의 리눅스 환경에 임의의 directory를 생성한다.
2. 해당 directory에 해당 파일들을 clone 한다.
```
1. git init
2. git clone https://github.com/8KJS3/oss_personal_project
```
3. Python과 pip3 library를 설치한다.
```
1. sudo apt install python3.8
2. pip3 install pygame
3. pip3 install pylance
```
4. 정상적으로 설치 되었다면 python3 game.py를 실행하면 게임 창이 뜨면서 실행된다.

### MacOS

# 실행 예시
![gameexample](https://github.com/8KJS3/oss_personal_project/assets/125852130/caaa1eb8-8a53-4cac-977c-1d9f4f0b8b37)

# 코드 설명
## game.py
### def init_Game - System
- Summary : 게임 기본 세팅을 초기화 하는 함수
  1. 글로벌 함수 선언 & 파이게임 초기 설정
  2. 게임 화면 크기 & 이름 설정
  3. 게임 틱 설정.

### def terminate - System
- Summary : 게임 창 & 프로그램 종료 
  1. Input : None
  2. Output : pygame과 system 종료.

### def gameOver - System & Display
- Summary : 게임 오버 창 출력 & 프로그램 종료
  1. Input : None
  2. Print : Display에 Game over 문자 가시화 
  3. Output : Program Restrart or Stop

### def drawplayer - Display
- Summary : 디스플레이에 플레이어 가시화
  1. Input : Player의 좌표 (x,y)
  2. Print : x, y좌표를 중심으로 하는 Player Object 가시화

### def b_e_crash_check - System
- Summary : Bullet - Enemy 충돌 확인
  1. Input : Bullet의 좌표 & Enemy의 좌표 (x,y)
  2. Output : ( True or False ) Bullet size를 고려해 충돌 여부 반환  

### def p_e_crash_check - System
- Summary : Player - Enemy 충돌 확인
  1. Input : Player의 좌표 & Enemy의 좌표 (x,y)
  2. Output : ( True or False ) Player size를 고려해 충돌 여부 반환 

### def print_time - Display
- Summary : Play-time 실시간 출력
  1. Input : Play-time
  2. Print : Display에 Play-time 문자 형태로 가시화

### def print_exp - Display
- Summary : Player level & exp 출력
  1. Input : Player level, current exp, max exp
  2. Print : Display에 Level, current exp, max exp 문자 형태로 가시화

### def level_up - System, Display
- Summary : Player level-up 시 플레이어 강화 선택지 출력 
  1. Input : None
  2. Print : Level-up 스펙업 선택지 출력
  3. Output : ( 1 ~ 3 ) 선택지 값 반환

### def run_Game - Total
- Summary : 게임 실행 함수
  1. Declare : Display, time info, player info, bullet info
  2. Input : Keydown event
  3. Feature1 : Player Movement
  ```
  - 기본 조작키 : w, s, a, d
  - 이동&출력 : 키 입력에 따라 플레이어 속도에 비례해 좌표를 이동시키고 해당 좌표에 플레이어를 출력함.
  ```
  4. Feature2 : Bullet Shoot
  ```
  - 기본 조작키 : space
  - 이동&출력 : 키 입력 당시 플레이어 방향에 따라 총알을 일직선으로 좌표 이동 & 출력
  ```
  5. Feature3 : Enemy Create
  ```
  - 조건 : enemy count ( 현재 Display에 생성된 적 수 ) < enemy limit ( 한 번에 Display 위에 존재 가능한 적 수 )
  - 생성 : 방향 지정 (Left,Right,Up,Down) > 좌표 지정 (방향 범위 내 랜덤 좌표) > 생성
  - 이동 : enemy speed 비례해서 생성 위치 대칭점을 향해 일직선으로 이동
  - 소멸 : 대칭점 도착 시 enemy delete & enemy count 감소 & enemy 생성 
  ```
  6. Feature4 : Bullet - Enemy Relation
  ```
  - 조건 : Distance < Bullet Size*2
  - 소멸 : 충돌한 Bullet & Enemy 소멸
  - 조정 : Player exp 상승
  ```
  7. Feature5 : Player - Enemy Relation
  ```
  - 조건 : Distance < Player Size
  - 출력 : Game Over 함수 출력
  ```
  8. Feature6 : Level Up
  ```
  - 조건 : Player exp > max exp
  - 조정 : Player level + 1 & Player exp - max exp & max exp increse
  ```
  
