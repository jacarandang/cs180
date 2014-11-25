import os, sys
import pygame
from pygame.locals import *
from classes.base import *
from classes.tower import *
#import classes

class Game:

	def __init__(self, screen):
		self.screen = screen
		self.running = True
		self.clock = pygame.time.Clock()
		
		self.bg = pygame.Surface((800, 600)) #temporary BG
		self.bg = self.bg.convert()
		self.bg.fill((255, 255, 255))

		self.image = pygame.image.load('res/bg1.jpg')
		self.imageRect = self.image.get_rect()

		self.m_pos = (-10,-10)    #Mouse Coordinates
		self.m_down = False	#Left Mouse Button Down

		self.grid = Board(22,18,(1,0))  #Board
		
		self.select_T = None	#Tower Selected

		self.T_list = [] #Towers on Grid
		
	def checkEvents(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.running = False

			if event.type == MOUSEMOTION:
				self.m_pos = (event.pos[0], event.pos[1])
				#print self.m_pos

			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					print 'left mouse button'
					self.m_down = True
					

			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.running = False

				if event.key == K_1:
					print 'T_1'
					self.select_T = Tower()

				if event.key == K_2:
					print 'T_2'
					self.select_T = Tower(2,2)

				if event.key == K_3:
					print 'T_3'
					self.select_T = Tower(1,3)

				if event.key == K_4:
					print 'T_4'
					self.select_T = Tower(2,3)

				if event.key == K_5:
					print 'T_5'
					self.select_T = Tower(3,3)

	def start(self):
		while(self.running):
			self.clock.tick(60)
			self.checkEvents()
			
			self.screen.blit(self.image, self.imageRect)			
			#self.screen.blit(self.image, (0,0), (400,300,300,300))
			#self.screen.blit(self.bg, (0, 0))
			#self.grid.draw(30,self.screen)

			for i in self.T_list:
				i.drawBox(0,0,self.screen)

			if self.select_T != None:
				boxContain = self.grid.detect(self.m_pos,self.select_T,self.screen)
				if self.m_down:
					overlap = False
					for i in self.T_list:
						for j in i.occupy:
							for k in boxContain:
								if j == k:
									overlap = True
					if not overlap:
						for i in boxContain:
							self.select_T.occupy.append(i)

						for i in boxContain:
							self.grid.set(i[0],i[1],1)

						self.T_list.append(self.select_T)
						self.select_T = None
					else:
						print 'Overlap Error'

					self.m_down = False
			
			pygame.display.update()
  
  
if __name__ == '__main__':	

	pygame.init()
	pygame.display.set_caption("Game Title")
	SCREEN = pygame.display.set_mode((800, 600))
	#pygame.display.toggle_fullscreen()
	
	game = Game(SCREEN)
	game.start()





















