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
enemy2_surface = pygame.image.load('graphics/enemy2/Fly1.png').convert_alpha()
enemy3_surface = pygame.image.load('graphics/enemy2/Fly1.png').convert_alpha()
enemy4_surface = pygame.image.load('graphics/enemy1/snail1.png').convert_alpha()
#variable for position of enemy one to be able to animate movement
enemy1_var_pos =600
enemy2_var_pos = 600
enemy3_var_pos = 600
enemy4_var_pos = 600
enemy2_var_hight = 264
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
    screen.blit(text_surface,(350,50))

    #move enemy1 location -5 with each interval
    enemy1_var_pos -= 5
    enemy2_var_pos -= 10
    enemy3_var_pos -= 13
    enemy4_var_pos -= 7
    enemy2_var_hight -= 2
    # if statement to make sure snail comes back 
    if enemy1_var_pos < -100 : enemy1_var_pos = 800
    screen.blit(enemy1_surface,(enemy1_var_pos,264))
    if enemy2_var_pos < -100 : enemy2_var_pos = 800
    if enemy2_var_hight < 20 : enemy2_var_hight = 264
    screen.blit(enemy2_surface,(enemy2_var_pos,enemy2_var_hight))
    if enemy3_var_pos < -100 : enemy3_var_pos = 800
    screen.blit(enemy3_surface,(enemy3_var_pos,50))
    if enemy4_var_pos < -100 : enemy4_var_pos = 800
    screen.blit(enemy4_surface,(enemy4_var_pos,264))
    
    pygame.display.update()
    #use clock.tick to set frame rate to make sure game runs consistant
    clock.tick(60) 