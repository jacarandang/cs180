import os, sys
import pygame
from pygame.locals import *
import classes

class Game:

	def __init__(self, screen):
		self.screen = screen
		self.running = True
		self.clock = pygame.time.Clock()
		
		self.bg = pygame.Surface((800, 600)) #temporary BG
		self.bg= self.bg.convert()
		self.bg.fill((255, 255, 255))
		
	def checkEvents(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.running = False
  
	def start(self):
		while(self.running):
			self.clock.tick(60)
			self.checkEvents()
			
			self.screen.blit(self.bg, (0, 0))
			pygame.display.update()
  
  
if __name__ == '__main__':
	

	pygame.init()
	pygame.display.set_caption("Game Title")
	SCREEN = pygame.display.set_mode((800, 600))
	pygame.display.toggle_fullscreen()
	
	game = Game(SCREEN)
	game.start()