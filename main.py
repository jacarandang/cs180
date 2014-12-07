import os, sys
import pygame
from pygame.locals import *
from classes.base import *
from classes.tower import *
from classes.virus import *
from classes import virusAI
from classes.UI import *
from classes.thing import *
#import classes

class Game:

	def __init__(self, screen, values = None):
		self.screen = screen
		self.running = True
		self.clock = pygame.time.Clock()
		
		self.bg = pygame.Surface((800, 600)) #temporary BG
		self.bg = self.bg.convert()
		self.bg.fill((88, 0, 0))

		self.image = pygame.image.load('res/bg.png').convert_alpha()
		self.imageRect = self.image.get_rect()

		self.values = values
		self.m_pos = (-10,-10)    #Mouse Coordinates
		self.m_down = False	#Left Mouse Button Down
		self.m_pos_down = (-10,-10)  #Mouse Down Coordinates

		self.grid = Board(22,18,(1,0))  #Board
		self.thing = ThingSprite(100)
		
		self.select_T = None	#Tower Selected

		self.T_list = [] #Towers on Grid
		self.tgroup = pygame.sprite.Group()
		
		self.bgroup = pygame.sprite.Group()

		self.vplayer = virusAI.Player(self.grid, self.thing, self.tgroup, self.values)
		self.vgroup = []
		
		self.allsprite = pygame.sprite.Group()
		self.allsprite.add(self.thing)
		
		self.status = "prep"	#"prep" or "wave"
		self.preptime = 5
		self.wavetime = 20
		self.timer = time()
		
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
						self.select_T = Tower(1,1,30,1,'nml',6)
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

				if event.key == K_7:
					if self.select_T == None:
						self.select_T = StemCell()
					else:
						self.select_T = None

				if event.key == K_8:
					if self.select_T== None:
						self.select_T = Lymphocyte()
					else:
						self.select_T = None
				
				if event.key == K_9:
					if self.select_T == None:
						self.select_T = Granulocyte()
					else:
						self.select_T = None

				if event.key == K_0:
					if self.select_T == None:
						self.select_T = NaturalKillerCell()
					else:
						self.select_T = None

				if event.key == K_q:
					if self.select_T == None:
						self.select_T = TCell()
					else:
						self.select_T = None

				if event.key == K_w:
					if self.select_T == None:
						self.select_T = BCell()
					else:
						self.select_T = None

				if event.key == K_e:
					if self.select_T == None:
						self.select_T = PlasmaCell()
					else:
						self.select_T = None

				if event.key == K_r:
					if self.select_T == None:
						self.select_T = Granulocyte()
					else:
						self.select_T = None

				if event.key == K_t:
					if self.select_T == None:
						self.select_T = Basophil()
					else:
						self.select_T = None

				if event.key == K_y:
					if self.select_T == None:
						self.select_T = Neutrophil()
					else:
						self.select_T = None

				if event.key == K_u:
					if self.select_T == None:
						self.select_T = Eosinophil()
					else:
						self.select_T = None

				if event.key == K_i:
					if self.select_T == None:
						self.select_T = Monocyte()
					else:
						self.select_T = None

				if event.key == K_o:
					if self.select_T == None:
						self.select_T = Macrophage()
					else:
						self.select_T = None

				if event.key == K_p:
					if self.select_T == None:
						self.select_T = Megakaryocyte()
					else:
						self.select_T = None

				if event.key == K_a:
					if self.select_T == None:
						self.select_T = Thrombocyte()
					else:
						self.select_T = None
					
				if event.key == K_z:
					for g in self.vgroup:
						for v in g:
							v.stun(1)
					
	def hasVirus(self):
		v = False
		for g in self.vgroup:
			if len(g) != 0:
				v = True
				break
		
		return v
		
		
	def start(self):
		while(self.running):
			self.clock.tick(60)
			self.checkEvents()
			
			if self.status == "prep":
				if time() - self.timer >= self.preptime:
					self.timer = time()
					self.status = "wave"
					self.vgroup.append(self.vplayer.getNextGroup())
			else:
				if time() - self.timer >= self.wavetime or not self.hasVirus():	#or if no virus exist
					self.timer = time()
					self.status = "prep"
					print "prep"
					
			
			#Draws all Towers in Grid
			self.screen.blit(self.bg, (0, 0))
			
			self.allsprite.update()
			self.allsprite.draw(self.screen)

			
			self.bgroup.update()
			self.screen.blit(self.image, self.imageRect)
			
			self.bgroup.draw(self.screen)
			
			for i in self.T_list:
				if i.view_atk:
					i.drawAtk(0,0,self.screen)
				#i.drawBox(0,0,self.screen)
			
			for g in self.vgroup:
				g.update()
				g.draw(self.screen)

		
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
						self.tgroup.add(self.select_T)
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

			for j in self.T_list:
				vlist = []
				for z in self.vgroup:
					shoot = False
					for i in z:
						if pygame.sprite.collide_circle(i,j):
							if j.tower_type == 'Neutrophil':
								vlist.append(i)
							else:
								j.Shoot(i,self.bgroup)
								shoot = True
								break
					if shoot: break
				if j.tower_type == 'Neutrophil':
					j.Shoot(vlist, self.bgroup)
			
			self.tgroup.update()
			self.tgroup.draw(self.screen)
	
			pygame.display.update()
  
  
if __name__ == '__main__':	

	pygame.init()
	pygame.display.set_caption("Game Title")
	SCREEN = pygame.display.set_mode((800, 600))
	#pygame.display.toggle_fullscreen()
	
	game = Game(SCREEN)
	game.start()





















