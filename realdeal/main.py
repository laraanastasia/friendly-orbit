import pygame,sys
from settings import *
class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('little divine Seraphina')
		self.clock = pygame.time.Clock()

def run(self):
        while True: #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '_main_': #check if this is our main file
    game = Game()
    game.run()