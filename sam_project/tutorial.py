import pygame
import brickbreak

back_width = 600 # 가로 크기
back_height = 800 # 세로 크기

#pygame 창 설정
pygame.display.set_caption("brick break") #게임 이름
background = pygame.display.set_mode((back_width, back_height))

#이미지 불러오기
Left_Key = pygame.image.load('left.png')
Left_Key = pygame.transform.scale(Left_Key, (50,50))
Right_Key = pygame.image.load('right.png')
Right_Key = pygame.transform.scale(Right_Key, (50,50))
start_image = pygame.image.load('startbut.png').convert_alpha()

#버튼 클래스
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image,(int(width * scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        #마우스 위치 받기
        pos = pygame.mouse.get_pos()

        #마우스가 버튼 위에 있는지 확인/버튼위에서 왼쪽 마우스클릭 시 게임시작
        if self.rect.collidepoint(pos) :
            if pygame.mouse.get_pressed()[0] == 1:
                brickbreak.main_S1()

        #버튼 그리기
        background.blit(self.image, (self.rect.x, self.rect.y))

start_button = Button(230, 620, start_image, 1)

#폰트 설정
Title_Font = pygame.font.SysFont(None, 60)
Explan_Font = pygame.font.SysFont(None, 35)

#텍스트 설정
Title_Txt = Title_Font.render("<<< TUTORIAL >>>",True,(0,0,0))
Explan_Txt = Explan_Font.render(" : Move to ", True, (0,0,0,))
RIGHT_Txt = Explan_Font.render("RIGHT", True, (136, 0, 21))
LEFT_Txt = Explan_Font.render("LEFT", True, (63, 72,204))
careful_Txt = Explan_Font.render("DO NOT DROP YOUR BALL!", True, (0,0,0))
Control_Txt = Explan_Font.render("Control Test", True, (0,0,0))

def Tut_main():

    paddle_x = 270
    paddle_y = 530
    
    pygame.init()

    running = True
    while running:

        background.fill((112, 146, 190))

        #튜토리얼 설명 출력
        background.blit(Title_Txt, (120,50))

        background.blit(Right_Key, (160,155))
        background.blit(Explan_Txt, (250, 170))

        background.blit(Left_Key, (160,235))
        background.blit(Explan_Txt, (250, 250))

        background.blit(RIGHT_Txt, (380, 170))
        background.blit(LEFT_Txt, (380, 250))
        background.blit(careful_Txt, (135, 350))

        background.blit(Control_Txt,(240,450))
        
        #시작 버튼 생성
        start_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle_x -= 5
                elif event.key == pygame.K_RIGHT:
                    paddle_x += 5 
        
        #시험해보기 위한 패들 생성
        pygame.draw.rect(background,(242,242,0),(paddle_x, paddle_y,70,20))
        pygame.display.update()
