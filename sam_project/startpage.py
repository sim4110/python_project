import pygame
import tutorial

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 600 # 가로 크기
screen_height = 800 # 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀(제목) 설정
pygame.display.set_caption("brick break") #게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("start.png")

#pygame에서는 이벤트 루프가 있어야 창이 꺼지지않음
# 이벤트 루프
running = True # 게임이 진행중인지 확인하기
while running:
    for event in pygame.event.get(): # running 중 키보드나,마우스 입력값(이벤트)을 체크해주는것
        if event.type == pygame.MOUSEBUTTONDOWN:
            tutorial.Tut_main()
        
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는지
            running = False # 게임이 진행중이 아님

    #screen.fill((0, 0, 255)) #RGB형식으로 이미지 로드
    screen.blit(background, (0, 0)) # 배경 그리기(background 가 표시되는 위치)
    pygame.display.update() # 게임화면을 지속적으로 그리기(for문도는동안 계속)

# pygame 종료
pygame.quit()