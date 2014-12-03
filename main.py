import os, sys
import pygame
from pygame.locals import *
from classes.base import *
from classes.tower import *
from classes.virus import *
from classes import virusAI
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
		self.m_pos_down = (-10,-10)  #Mouse Down Coordinates

		self.grid = Board(22,18,(1,0))  #Board
		
		self.select_T = None	#Tower Selected

		self.T_list = [] #Towers on Grid
		
		self.vplayer = virusAI.Player(self.grid)
		
		self.vgroup = []
		
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
					self.m_pos_down = (event.pos[0], event.pos[1])

			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.running = False

				if event.key == K_1:
					print 'T_1'
					if self.select_T == None:
						self.select_T = Tower()
					else:
						self.select_T = None

				if event.key == K_2:
					print 'T_2'
					if self.select_T == None:
						self.select_T = Tower(2,2)
					else:
						self.select_T = None

				if event.key == K_3:
					print 'T_3'
					if self.select_T == None:
						self.select_T = Tower(1,3)
					else:
						self.select_T = None

				if event.key == K_4:
					print 'T_4'
					if self.select_T == None:
						self.select_T = Tower(2,3)
					else:
						self.select_T = None

				if event.key == K_5:
					print 'T_5'
					if self.select_T == None:
						self.select_T = Tower(3,3)
					else:
						self.select_T = None
				
				if event.key == K_6:
					self.vgroup.append(self.vplayer.getNextGroup())
					
	def start(self):
		while(self.running):
			self.clock.tick(60)
			self.checkEvents()
			
			self.screen.blit(self.image, self.imageRect)			
			#self.screen.blit(self.image, (0,0), (400,300,300,300))
			#self.screen.blit(self.bg, (0, 0))
			#self.grid.draw(30,self.screen)

			#Draws all Towers in Grid
			for i in self.T_list:
				if i.view_atk:
					i.drawAtk(0,0,self.screen)
				i.drawBox(0,0,self.screen)

		
			#Place Tower in Grid
			if self.select_T != None:
				boxContain = self.grid.detect(self.m_pos,self.select_T,self.screen)
				if self.m_down:
					overlap = False
					#Checks if selection is outside of Grid
					for i in boxContain:
						if i == False:
							overlap = True

					#Checks if selection is overlapping an existing Tower
					for i in self.T_list:
						for j in i.occupy:
							for k in boxContain:
								if j == k:
									overlap = True
					if not overlap:
						self.select_T.setOccupy(boxContain)

						for i in boxContain:
							self.grid.set(i[0],i[1],1)

						self.T_list.append(self.select_T)
						self.select_T = None
					else:
						print 'Overlap/Outside Error'

					self.m_down = False
			else:
				if self.m_down:

					for i in self.T_list:
						for j in i.occupy:
							if j == self.grid.coorToIndex(self.m_pos_down, i.size):
								if i.view_atk:								
									i.view_atk = False
								else:
									i.view_atk = True								
								#i.drawAtk(0,0,self.screen)
								break

					self.m_down = False
			
			for g in self.vgroup:
				g.update()
				g.draw(self.screen)
			pygame.display.update()
  
  
if __name__ == '__main__':	

	pygame.init()
	pygame.display.set_caption("Game Title")
	SCREEN = pygame.display.set_mode((800, 600))
	#pygame.display.toggle_fullscreen()
	
	game = Game(SCREEN)
	game.start()





















