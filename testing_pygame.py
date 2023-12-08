import pygame
from sys import exit

#start pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
#set name of shell
pygame.display.set_caption("fast guy")
clock = pygame.time.Clock()

surface = pygame.Surface((100,200))
surface.fill('Red')

#run code invinitively to make gaming possible
while True:
    # never run code without this-you wont be able to close it on its own
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #blit= block image transfer: put one thingy onto another thingy
    screen.blit(surface,(200,100))
    pygame.display.update()
    #use clock.tick to set frame rate to make sure game runs consistant
    clock.tick(60)