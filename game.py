import pygame
from sys import exit

#start pygame

pygame.init()
screen = pygame.display.set_mode((800,400))

#set name of shell

pygame.display.set_caption("fast guy")
clock = pygame.time.Clock()

#creating text: 1. create font ; 2. write text on surface ; 3. blit text on screen
font = pygame.font.Font('font/Pixeltype.ttf',50)
#import image onto suface (convert makes the image easier for python to work with)
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
#text you want to display ; smothe edges ; color
text_surface = font.render('Fast Guy',False,'Black') 
enemy1_surface = pygame.image.load('graphics/enemy1/snail1.png').convert_alpha() # _alpha to ignore the alpha part of the image
#variable for position of enemy one to be able to animate movement
enemy1_var_pos =600
#run code infinitive to make gaming possible
while True:
    # never run code without this-you wont be able to close it on its own
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #blit= block image transfer: put one thingy onto another thingy
    #order you call code here is important!
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    #move enemy1 location -5 with each interval
    enemy1_var_pos -= 5
    # if statement to make sure snail comes back 
    if enemy1_var_pos < -100 : enemy1_var_pos = 800
    screen.blit(enemy1_surface,(enemy1_var_pos,250))
    pygame.display.update()
    #use clock.tick to set frame rate to make sure game runs consistant
    clock.tick(60) 