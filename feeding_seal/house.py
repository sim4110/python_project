#roc_house program

import pygame
from pygame.local

#background
back_width = 1920
back_height = 1080

#pygame setting
pygame.display.set_caption("Feeding Seal") #game_name
background = pygame.set_mode((back_width, back_height))

#pygame background image
background = pygame.image.load('home.png')

#pygame running
running = True 
while running :
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
