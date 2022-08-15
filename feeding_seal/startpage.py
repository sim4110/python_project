#start page
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

##character image
Racc = pygame.image.load('raccoons.png')

##item image
message_fromseal = pygame.image.load('mission.png')


##button image
startButton = pygame.image.load('startbut.png')
exitButton = pygame.image.load('exitbut.png')

#Raccoons setting
Rac_x, Rac_y = 0,0
Rac_width = 900
Rac_height = 900
Rac_size = 0.3 
Racc = pygame.transform.scale(Racc,(Rac_width*Rac_size, Rac_height*Rac_size))

#messagesetting
clear = False
mission_card_width=900
mission_card_height=1080
mission_card_size = 0.4
message_fromseal= pygame.transform.scale(message_fromseal,(mission_card_width*mission_card_size, mission_card_height*mission_card_size))








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
            Game_run1()
  
        pygame.display.update() 


#inside the Raccoons's house
def Game_run1(): 
    global run, Racc
    Rac_x, Rac_y = 200, 200

    while run:
        background.fill((255,255,255))
        background.blit(homeRac,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:                  
                if event.key == pygame.K_q:
                    background.fill((255,255,255))
                    run = False
                if event.key == pygame.K_DOWN:
                    Rac_y +=100
                elif event.key == pygame.K_UP:
                    Rac_y -=100
                elif event.key == pygame.K_LEFT:
                    Rac_x -=100
                elif event.key == pygame.K_RIGHT:
                    Rac_x +=100
        
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
            Game_run2() 

        background.blit(Racc,(Rac_x, Rac_y)) 
        pygame.display.update() 

#page2 : front of Raccoons's house
def Game_run2():
    global run
    global Rac_x,Rac_y
    Rac_x = 130
    Rac_y = 660

    while run:
        background.blit(homeRacFront,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                #return to Raccoons's house
                if event.key == pygame.K_SPACE and Rac_x <=130 and Rac_x >=100:
                    Game_run1()
                if event.key == pygame.K_SPACE and Rac_x <=600 and Rac_x >= 450:
                        #background.blit(message_fromseal,(700,200))
                        if clear==False:
                            check_message(message_fromseal)
                        
                if event.key == pygame.K_q:
                    background.fill((255,255,255))
                    run = False
                if event.key == pygame.K_RIGHT:
                    Rac_x+=100
                if event.key == pygame.K_LEFT:
                    Rac_x-=100

        #Raccoons don't left the screen
        if Rac_x<=0:
            Rac_x = 0
        if Rac_x>=1600:
            Rac_x = 1600

        background.blit(Racc,(Rac_x, Rac_y)) 
        pygame.display.update()


def check_message(message):
    global Rac_x, Rac_y, run
    while run:
        background.blit(message,(700,200))
        background.blit(Racc,(Rac_x, Rac_y)) 
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                if event.key == pygame.K_q:
                    run = False
        
        pygame.display.update()
    



#main
GameStartPage()