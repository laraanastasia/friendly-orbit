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
#import image onto suface
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
#text you want to display ; smothe edges ; color
text_surface = font.render('Fast Guy',False,'Green')

#run code invinitively to make gaming possible
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
    pygame.display.update()
    #use clock.tick to set frame rate to make sure game runs consistant
    clock.tick(60)