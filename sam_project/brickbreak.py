from ast import Sub
import sys
import math
import random
from webbrowser import BackgroundBrowser
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, Rect, KEYUP
import time

#버튼 클래스
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height =image.get_height()

        self.image = pygame.transform.scale(image,(int(width * scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked  = False

    def draw(self, surface):
        action = False
        #마우스 위치 받기
        pos = pygame.mouse.get_pos()

        #마우스가 버튼 위에 있는지 학인/버튼클릭 확인
        if self.rect.collidepoint(pos) :
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #버튼 그리기
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action
        
class Block:
    # 블록, 공, 패들 오브젝트
    def __init__(self, col, rect, speed=0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-10, 10) + 270

    def move(self):
        #  공을 움직인다 
        self.rect.centerx += math.cos(math.radians(self.dir))\
             * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir))\
             * self.speed

    def draw(self):
        #  블록, 공, 패들을 그린다 
        if self.speed == 0:
            pygame.draw.rect(Background, self.col, self.rect)
        else:
            pygame.draw.ellipse(Background, self.col, self.rect)

#stage 진입화면
def start_stage(snum):
    Stage_font = pygame.font.SysFont(None, 80)
    Stage_txt = Stage_font.render('STAGE ' + str(snum), True, (0,0,0))
    Background.blit(Stage_txt, (180,350))
    
# 피버 타임 이벤트
def feverTime():
    global BALLS

    # 공 두개를 추가해주고
    for i in range(2):
        BALLS.append(Block((0, 0, 0), Rect(300, 400, 20, 20), 10))

    # 공의 속도를 9로 맞춘다.
    for BALL in BALLS:
        BALL.speed = 9

def tick():

    #  프레임별 처리 
    global start,BALLS, BLOCKS, score, Check_Fever, Fever_Start, Fever_End

    # 키 입력 처리
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                PADDLE.rect.centerx -= 5
            elif event.key == K_RIGHT:
                PADDLE.rect.centerx += 5        
 
    for BALL in BALLS:
        if BALL.rect.centery < 1000:
            BALL.move()

        # 블록과 충돌하면
        prevlen = len(BLOCKS)
        BLOCKS = [x for x in BLOCKS
                if not x.rect.colliderect(BALL.rect)]
        if len(BLOCKS) != prevlen:
            BALL.dir = - BALL.dir
            score += 100 # get score + 100

        # 점수가 일정치이고, 피버타임이 아니면 피버타임실행
        if (score//1000 >0 and score%1000 == 100) and Check_Fever == False:
            Check_Fever = True
            Background.fill((127,127,127))
            feverTime()
        # 5초를 카운트하고 5초 뒤에는 피버타임 종료
        elif Check_Fever == True:    
            if Fever_Start == 0.0:
                Fever_Start = time.time()
            elif Fever_Start != 0.0:
                Fever_End = time.time()
                if Fever_End - Fever_Start >= 5: # 5초
                    Check_Fever = False

        # 패들과 충돌하면
        if PADDLE.rect.colliderect(BALL.rect):
            BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) \
                / PADDLE.rect.width * 80

        # 벽과 충돌하면
        if BALL.rect.centerx < 0 or BALL.rect.centerx > 600:
            BALL.dir = 180 - BALL.dir
        if BALL.rect.centery < 0:
            BALL.dir = -BALL.dir
            BALL.speed = 15

         #패들이 화면밖으로 나가면
        if PADDLE.rect.centerx < 35:
            PADDLE.rect.centerx = 35
        elif PADDLE.rect.centerx >565:
            PADDLE.rect.centerx = 565

pygame.init()
pygame.key.set_repeat(5, 5)

Background = pygame.display.set_mode((600, 800))
Background.fill((255,255,255))
FPSCLOCK = pygame.time.Clock()

#버튼 이미지 불러오기
restart_image = pygame.image.load('restartbnt.png').convert_alpha()
exit_image = pygame.image.load('exitbnt.png').convert_alpha()

Restart_Bnt = Button(160,420,restart_image,1.2)
Exit_Bnt = Button(320,420,exit_image,1.2)

BLOCKS = [] 
PADDLE = Block((242, 242, 0), Rect(300, 750, 70, 20))
BALLS = [Block((242, 242, 0), Rect(300, 400, 20, 20), 9)]

start = True
Check_Restart = False
Check_Fever = False

score = 0
Fever_Start = 0.0
Fever_End = 0.0

# 초기화
def init():
    global Background, FPSCLOCK, BLOCKS, PADDLE, BALLS, start, Check_Restart, Check_Fever, Last_score, score, Fever_Start, Fever_End

    pygame.init()
    pygame.key.set_repeat(5, 5)
    Background = pygame.display.set_mode((600, 800))
    FPSCLOCK = pygame.time.Clock()
    BLOCKS = []
    PADDLE = Block((242, 242, 0), Rect(300, 750, 70, 20))
    BALLS = [Block((242, 242, 0), Rect(300, 400, 20, 20), 9)]
    
    start = True
    Check_Restart = False
    Check_Fever = False

    Last_score  = score 
    score = 0
    Fever_Start = 0.0
    Fever_End = 0.0

# 게임 1단계
def main_S1():
    global Check_Restart, score, Check_Fever, Fever_Start, Fever_End, start, Last_score
    """ 메인 루틴 """
    Main_font = pygame.font.SysFont(None, 80)
    Sub_font = pygame.font.SysFont(None, 36)
    Score_Font = pygame.font.SysFont(None, 25)
    Step_Clear = Main_font.render("Cleared!", True, (255, 255, 0))
    GameOver = Main_font.render("Game Over!", True, (0, 0, 0))
    Goal_score = Score_Font.render("Goal : 2500", True, (255,255,255))
    fps = 60
    colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0),
              (0, 128, 0), (128, 0, 128), (0, 0, 250)]

    # 블록을 추가
    for ypos, color in enumerate(colors, start = 0):
        for xpos in range(0, 5):
            BLOCKS.append(Block(color, Rect(xpos * 100 + 60, ypos * 50 + 40, 80, 30)))

    while True:
        tick()

          #시작전 카운팅
        if start:
            start = False
            for cnt in range(4,0,-1):
                if cnt == 4:
                    Background.fill((112, 146, 190))
                    start_stage(1)
                    pygame.display.update()
                    pygame.time.delay(1000)
                else :
                    Background.fill((112, 146, 190))
                    Cnt_txt = Main_font.render(str(cnt), True, (0,0,0))
                    Background.blit(Cnt_txt, (290,360))
                    pygame.display.update()
                    pygame.time.delay(1000)
            
        # 공을 그린다
        Background.fill((112, 146, 190))
        for BALL in BALLS:
            BALL.draw()
        PADDLE.draw()

        # 블록을 그린다
        for block in BLOCKS:
            block.draw()        

        # 블록을 모두 제거하면 성공
        if len(BLOCKS) == 0:
            Last_score = score
            Background.blit(Step_Clear, (200, 400))
            pygame.time.delay(1000)
            init()
            main_S2()
        
        # 공이 패들 밑으로 내려가면 해당 공은 삭제
        for BALL in BALLS:
            if BALL.rect.centery > 800 and len(BLOCKS) > 0:
                BALLS.remove(BALL)

        # 피버타임이 끝난 경우
        if Check_Fever == False and Fever_Start != 0.0 and Fever_End != 0.0:
            # 공 하나만 제외하고 모두 제거
            for BALL in BALLS:
                if(len(BALLS) == 1):
                    break
                elif(len(BALLS) > 1):
                    BALLS.remove(BALL)
            
            Fever_Start = 0.0
            Fever_End = 0.0

            # 속도 9으로 원복
            for BALL in BALLS:
                BALL.speed = 9

        # 공이 하나도 없는 경우(끝난 경우)
        if len(BALLS) <= 0:
            if score >=2500:
                Background.blit(Step_Clear, (200, 400))
                pygame.display.update()

                pygame.time.delay(1000)
                init()
                main_S2()

            else:
                Result_point = Sub_font.render("Your Point : " +str(score), True, (255,255,255))
                Background.fill((127,127,127))
                Background.blit(GameOver, (140, 300))
                Background.blit(Result_point, (210,360))
                if Restart_Bnt.draw(Background) == True:
                    print('restart')
                    Check_Restart = True

                if Exit_Bnt.draw(Background) == True:
                    print('exit')
                    pygame.quit()
                    sys.exit()

        # 스코어 보드
        Score = Score_Font.render("score : " + str(score), True, (255, 255, 255))
        Background.blit(Score, (10, 10))
        Background.blit(Goal_score,(200,10))

        pygame.display.update()
        FPSCLOCK.tick(fps)

        # 재시작버튼 동작 가능하도록 설정
        while Check_Restart:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            Check_Restart = False
            if Check_Restart == False:
                init()
                main_S1()

#게임 2단계
def main_S2():
    global Check_Restart, score, Check_Fever, Fever_Start, Fever_End, start

    Main_font = pygame.font.SysFont(None, 80)
    Sub_font = pygame.font.SysFont(None, 36)
    Score_Font = pygame.font.SysFont(None, 25)
    Step_Clear = Main_font.render("Cleared!", True, (255, 255, 0))
    GameOver = Main_font.render("Game Over!", True, (0, 0, 0))
    Goal_txt = Score_Font.render("Goal : Break all Bricks", True, (255,255,255))

    fps = 60

    #벽돌 1행 추가
    colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0),
              (0, 128, 0), (128, 0, 128), (0, 0, 250), (0,0,0)]

    #벽돌 지정
    for ypos, color in enumerate(colors, start=0):
        for xpos in range(0, 6):
            BLOCKS.append(Block(color, Rect(xpos * 100 + 10, ypos * 50 + 40, 80, 30)))

    start = True
    while True:
        tick()

        if start:
            start = False
            for cnt in range(4,0,-1):
                if cnt == 4:
                    Background.fill((112, 146, 190))
                    start_stage(2)
                    pygame.display.update()
                    pygame.time.delay(1000)
                else:
                    Background.fill((112, 146, 190))
                    Cnt_txt = Main_font.render(str(cnt), True, (0,0,0))
                    Background.blit(Cnt_txt, (290,360))
                    pygame.display.update()
                    pygame.time.delay(1000)

        Background.fill((112, 146, 190))

        #공 생성
        for BALL in BALLS:
            BALL.draw()

        #패달 생성
        PADDLE.draw()

        # 벽돌 생성
        for block in BLOCKS:
            block.draw()        

        # 블록을 모두 제거하면 성공
        if len(BLOCKS) == 0:
            Background.blit(Step_Clear, (200, 400))
            pygame.display.update()

        # 공이 패달 밑으로 내려가면 해당 공은 삭제
        for BALL in BALLS:
            if BALL.rect.centery > 800 and len(BLOCKS) > 0:
                BALLS.remove(BALL)

        # 피버타임이 끝난 경우
        if Check_Fever == False and Fever_Start != 0.0 and Fever_End != 0.0:
            # 공 하나만 제외하고 모두 제거
            for BALL in BALLS:
                if(len(BALLS) == 1):
                    break
                elif(len(BALLS)>=2):
                    BALLS.remove(BALL)
            Fever_Start = 0.0
            Fever_End = 0.0
            # 속도 9으로 원복
            for BALL in BALLS:
                BALL.speed = 9

        # 공이 하나도 없는 경우(끝난 경우)
        if len(BALLS) <= 0:
            score_Result = score+Last_score
            Result_point = Sub_font.render("Your Point : " +str(score_Result), True, (255,255,255))
            Background.fill((127,127,127))
            Background.blit(GameOver, (140, 300))
            Background.blit(Result_point, (210,360))
            if Restart_Bnt.draw(Background) == True:
                print('restart')
                Check_Restart = True

            if Exit_Bnt.draw(Background) == True:
                print('exit')
                pygame.quit()
                sys.exit()

        # 스코어 보드
        Score = Score_Font.render("score : " + str(score + Last_score), True, (255, 255, 255))
        Background.blit(Score, (10, 10))
        Background.blit(Goal_txt, (200, 10))


        pygame.display.update()
        FPSCLOCK.tick(fps)
        
        # restart버튼 누르면 재시작 가능하도록 설정
        while Check_Restart:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            Check_Restart = False
            if Check_Restart == False:
                score = 0
                init()
                main_S2()