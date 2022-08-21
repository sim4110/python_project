#start page
from re import X
from unittest.mock import seal
import pygame
pygame.init()

#pygame screen setting
back_size = [1920, 1080]
background = pygame.display.set_mode(back_size)
pygame.display.set_caption("Feeding Seal") #game_name
run = True

#image load
##background image
startPage = pygame.image.load('startpage.png')
homeRac = pygame.image.load('home.png')
homeRacFront = pygame.image.load('home_out.png')
farmFront = pygame.image.load('farm_frant.png')
farmIn = pygame.image.load('farm_in.png')
road = pygame.image.load('horizen.png')
homeSealFront = pygame.image.load('seal_home_out.png')
homeSeal = pygame.image.load('seal_home.png')

##character image
Racc = pygame.image.load('raccoons.png')
# Racc_right = pygame.image.load('raccoons.png')
Racc_left = pygame.image.load('raccoons_left.png')
Seal = pygame.image.load('seal.png')

##item image
message_fromseal = pygame.image.load('mission.png')
message_clear = pygame.image.load('respond.png')

chicken = pygame.image.load('chicken.png')
chicken_size = 0.4
chicken = pygame.transform.scale(chicken, (900*chicken_size, 900*chicken_size))
chicken_inven = pygame.transform.scale(chicken,(80,80))

gyul = pygame.image.load('gyul.png')
gyul_size = 0.4
gyul = pygame.transform.scale(gyul,(900*gyul_size, 900*gyul_size))
gyul_inven = pygame.transform.scale(gyul,(80,80))

message = pygame.image.load('message.png')

inven_box=pygame.image.load('inven_2.png')
ib_size = 0.7
inven_box=pygame.transform.scale(inven_box,(800*ib_size,500*ib_size))

##button image
startButton = pygame.image.load('startbut.png')
exitButton = pygame.image.load('exitbut.png')

#Raccoons setting
Rac_x, Rac_y = 0,0
Rac_width = 900
Rac_height = 900
Rac_size = 0.3 
Racc = pygame.transform.scale(Racc,(Rac_width*Rac_size, Rac_height*Rac_size))
Racc_left = pygame.transform.scale(Racc_left,(Rac_width*Rac_size, Rac_height*Rac_size))
Racc_right = pygame.transform.scale(Racc,(Rac_width*Rac_size, Rac_height*Rac_size))

#Seal setting
Seal_size = 0.3
Seal_width = 900
Seal_height= 900
Seal = pygame.transform.scale(Seal,(Seal_size*Seal_width, Seal_size*Seal_width))

#messagesetting
clear = False
mission_card_width=900
mission_card_height=1080
mission_card_size = 0.6
message_fromseal= pygame.transform.scale(message_fromseal,(mission_card_width*mission_card_size, mission_card_height*mission_card_size))
message_clear = pygame.transform.scale(message_clear, (mission_card_width*mission_card_size, mission_card_height*mission_card_size))

#button class
class Button:
    def __init__(self, x, y, image, scale):
        width =image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image,(int(width * scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, surface):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check the mouse on the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0]== 0:
            self.clicked = False

        #draw the button
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

#start, exit button
Start_Btn = Button(800,700, startButton, 1)
Exit_Btn = Button(1000, 700, exitButton, 1)

#raccoon's bag
global Rac_bag
Rac_bag = [0,0]

#message setting
Msg = False
Msg_Btn = Button(670,400, message, 0.4)

#Start Page
def GameStartPage():
    global run
    while run:
        background.fill((0,0,0))
        background.blit(startPage,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
            # if event.type ==pygame.MOUSEBUTTONDOWN:
            #     run = False
        
        if Exit_Btn.draw(background) == True:
            run = False

        if Start_Btn.draw(background) == True:
            Game_run1(200,200)
  
        pygame.display.update() 

#get item
##open refrigerator
def open_refri(item):
    global run, Rac_bag, Rac_x, Rac_y
    while run:
        background.blit(item,(800,10))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Rac_bag[0] = 1
                    print(Rac_bag)
                if event.key == pygame.K_ESCAPE:
                    return
        background.blit(Racc,(Rac_x, Rac_y))
        pygame.display.update()

##pick gyul
def pick(item):
    global run, Rac_bag, Rac_x, Rac_y
    while run:
        background.blit(item,(1300,400))
        background.blit(Racc,(Rac_x, Rac_y))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Rac_bag[1] = 1
                    print(Rac_bag)
                if event.key == pygame.K_ESCAPE:
                    return 
        pygame.display.update()
        

def check_inventory(x,y):
    global run, Rac_bag

    if y >= 900 :
        background.blit(inven_box, (600,800))
    else :
        background.blit(inven_box, (600,-100))

    if Rac_bag[0] == 1:
        background.blit(chicken_inven, (x,y))
    if Rac_bag[1] == 1:
        background.blit(gyul_inven,(x+105,y))
    return 
        
#inside the Raccoons's house
def Game_run1(x, y): 
    global run, Racc, Rac_x, Rac_y 
    Rac_x = x
    Rac_y = y
    while run:
        background.fill((255,255,255))
        background.blit(homeRac,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:                  
                if event.key == pygame.K_q:
                    background.fill((255,255,255))
                    run = False
                if event.key == pygame.K_SPACE and Rac_x <=1600 and Rac_x>=1500 and Rac_y<=200:
                    open_refri(chicken)
                if event.key == pygame.K_DOWN:
                    Rac_y +=100
                elif event.key == pygame.K_UP:
                    Rac_y -=100
                elif event.key == pygame.K_LEFT:
                    Rac_x -=100
                    Racc = Racc_left
                elif event.key == pygame.K_RIGHT:
                    Rac_x +=100
                    Racc = Racc_right
        check_inventory(630,35)
        #Raccoons don't left the screen
        if Rac_x<=0:
            Rac_x = 0
        if Rac_x>=1600:
            Rac_x = 1600
        if Rac_y<=0:
            Rac_y = 0
        if Rac_y>=800:
            Rac_y = 800

        #go to the next page  
        if Rac_x >= 1600 and Rac_y >= 800:
            background.fill((255,255,255))
            Game_run2(130,660) 
        if Rac_x<=0:
            Game_run3(1590,660)

        background.blit(Racc,(Rac_x, Rac_y)) 
        pygame.display.update() 

#page2 : front of Raccoons's house
def Game_run2(x,y):
    global run, Racc, Msg
    global Rac_x,Rac_y
    Rac_x = x
    Rac_y = y

    while run:
        background.blit(homeRacFront,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                #return to Raccoons's house
                if event.key == pygame.K_SPACE and Rac_x <=230 and Rac_x >=100:
                    Game_run1(1590,801)
                if event.key == pygame.K_SPACE and Rac_x <=600 and Rac_x >= 450:
                        if clear==False:
                            check_message(message_fromseal)
                        if clear==True:
                            check_message(message_clear)
                        
                if event.key == pygame.K_q:
                    background.fill((255,255,255))
                    run = False
                if event.key == pygame.K_RIGHT:
                    Rac_x+=100
                    Racc = Racc_right
                if event.key == pygame.K_LEFT:
                    Rac_x-=100
                    Racc = Racc_left
        if Msg == False:
            if Msg_Btn.draw(background) ==True:
                if clear == False :
                    check_message(message_fromseal)
                    Msg == True
                if clear==True:
                    check_message(message_clear)
                    Msg = True

        check_inventory(630,35)
        #Raccoons don't left the screen
        if Rac_x<=0:
            Game_run3(1590,660)
        if Rac_x>=1600:
           Game_run5(1,660)

        background.blit(Racc,(Rac_x, Rac_y)) 
        pygame.display.update()


def check_message(message):
    global Rac_x, Rac_y, run
    while run:
        background.blit(message,(700,200))
        background.blit(Racc,(Rac_x, Rac_y)) 
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   return
                if event.key == pygame.K_q:
                    run = False
        check_inventory(630,35)
        pygame.display.update()
    
#page3 : go to the farm
def Game_run3(x,y):
    #print("page3")
    global Rac_x, Rac_y, run, Racc
    Rac_x = x
    Rac_y = y
    
    while run:
        background.blit(farmFront,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and Rac_x >= 1600:
                    Game_run2()
                #if event.key == pygame.K_SPACE and Rac_x <= 0:
                #    Game_run4()  
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_RIGHT:
                    Rac_x+=100
                    Racc = Racc_right
                    #print("right")
                if event.key == pygame.K_LEFT:
                    Rac_x-=100
                    Racc = Racc_left
                    #print("left")
        check_inventory(630,35)
        if Rac_x <= 0:
            Game_run4(1590,660)
        if Rac_x >=1600:
            Game_run2(10,660)

        background.blit(Racc,(Rac_x, Rac_y)) 
        pygame.display.update()
    
#page4 : get gyul for seal
def Game_run4(x,y):
    global Rac_x, Rac_y, run, Racc
    Rac_x = x
    Rac_y = y
    while run:
        background.blit(farmIn,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_SPACE and Rac_x <= 1400 and Rac_x >=1200:
                    pick(gyul)
                if event.key == pygame.K_RIGHT:
                    Rac_x+=100
                    Racc = Racc_right
                if event.key == pygame.K_LEFT:
                    Rac_x-=100
                    Racc = Racc_left
        check_inventory(630,35)
        if Rac_x >= 1600:
            Game_run3(1,660)
                    
        background.blit(Racc,(Rac_x, Rac_y)) 
        pygame.display.update()

#page5: go to the seal's house
def Game_run5(x,y):
    global Rac_x, Rac_y, run, Racc
    Rac_x = x
    Rac_y = y
    while run:
        background.blit(road,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_RIGHT:
                    Rac_x+=100
                    Racc = Racc_right
                if event.key == pygame.K_LEFT:
                    Rac_x-=100
                    Racc = Racc_left

        check_inventory(630,35)
        if Rac_x >=1600:
            Game_run6(1,540)
        if Rac_x <=0:
            Game_run2(1580,660)
        
        background.blit(Racc,(Rac_x, Rac_y)) 
        pygame.display.update()

#page6: seal's house
def Game_run6(x,y):
    global Rac_x, Rac_y, run, Racc
    Rac_x = x
    Rac_y = y
    while run:
        background.blit(homeSealFront,(0,0))
        background.blit(Seal,(900,540))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_SPACE and Rac_x >=1000 and Rac_x <1300:
                    Game_run7(1,800)
                if event.key == pygame.K_SPACE and Rac_x <=920 and Rac_x>=700:
                    give_food()
                if event.key == pygame.K_RIGHT:
                    Rac_x+=100
                    Racc = Racc_right
                if event.key == pygame.K_LEFT:
                    Rac_x-=100
                    Racc = Racc_left
        check_inventory(630,35)
        if Rac_x <=0:
            Game_run5(1580,660)
        
        background.blit(Racc,(Rac_x, Rac_y)) 
        pygame.display.update()

#give the food to seal
def give_food():
    global run, food_select, clear, Rac_bag, Racc, Msg
    while run:
        if Rac_bag[0] == 0 and Rac_bag[1] == 0:
            clear = True
            Msg == False
            return
        else :    
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        food_select = 0
                        #1 == chicken
                    elif event.key == pygame.K_RIGHT:
                        food_select = 1
                        #2 == gyul            
                    if event.key == pygame.K_SPACE:
                        Rac_bag[food_select] = 0
                    if event.key == pygame.K_ESCAPE:
                        return 
        background.blit(chicken,(600,400))
        background.blit(gyul, (1000,400))
        pygame.display.update()
                
def Game_run7(x,y):
    global Rac_x, Rac_y, run, Racc
    Rac_x = x
    Rac_y = y
    while run:
        background.fill((0,0,0))
        background.blit(homeSeal,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_RIGHT:
                    Rac_x+=100
                    Racc = Racc_right
                elif event.key == pygame.K_LEFT:
                    Rac_x-=100
                    Racc = Racc_left
                elif event.key == pygame.K_UP:
                    Rac_y-=100
                elif event.key == pygame.K_DOWN:
                    Rac_y+=100
        check_inventory(630,945)
        if Rac_x <= 0:
            Game_run6(1200,540)
        
        background.blit(Racc,(Rac_x, Rac_y)) 
        pygame.display.update()

#main
GameStartPage()