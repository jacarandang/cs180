import os, sys
import pygame
from pygame.locals import *
from classes.base import *
from classes.tower import *
from classes.virus import *
from classes import virusAI
from classes.UI import *
from classes.thing import *
from classes.ATP import *
from classes.trivia import *
from classes.member import Member
from classes.savestate import *
import pickle
from classes.towerAI import *
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
		self.testing = True
		if self.values == None:
			with file('ai/data.net') as f:
				pop = pickle.load(f)
				self.values = pop[0]
			self.testing = False
		self.m_pos = (-10,-10)    #Mouse Coordinates
		self.m_down = False	#Left Mouse Button Down
		self.m_pos_down = (-10,-10)  #Mouse Down Coordinates

		self.grid = Board(22,18,(1,0))  #Board
		self.thing = ThingSprite(100)
		
		self.select_T = None	#Tower Selected

		self.T_list = [] #Towers on Grid
		self.tgroup = pygame.sprite.Group()
		
		self.bgroup = pygame.sprite.Group()
		self.gameoptions = pygame.sprite.Group()
		self.pauseoptions = pygame.sprite.Group()
		
		self.vgroup = []
		
		self.allsprite = pygame.sprite.Group()
		self.allsprite.add(self.thing)
		
		self.status = "prep"	#"prep" or "wave"
		self.preptime = 5
		self.wavetime = 20
		self.timer = time()

		self.resource = ATP() #resource
		self.trivia = trivia()
		
		self.wave = 0
		self.currWave = -1
		self.wFont = pygame.font.Font('res/DS-DIGI.TTF', 30)
		self.wSurf = self.wFont.render(str(self.wave), True, (189,0,0))
		self.wRect = self.wSurf.get_rect()
		self.wRect.topleft = (730-self.wRect.centerx),463

		
		self.vplayer = virusAI.Player(self.grid, self.thing, self.tgroup, self.values, self.resource)
		self.fgroup = pygame.sprite.Group()
		self.fgroup.add(self.resource, self.trivia)
		
		self.pgroup = pygame.sprite.Group()

		self.go = False
		
		self.towerai = TowerPlayer(self.resource, self.T_list, self.tgroup, self.grid, self)
		
	def reinitialize(self):
		self.running = True
		self.clock = pygame.time.Clock()
		
		self.bg = pygame.Surface((800, 600)) #temporary BG
		self.bg = self.bg.convert()
		self.bg.fill((88, 0, 0))

		self.image = pygame.image.load('res/bg.png').convert_alpha()
		self.imageRect = self.image.get_rect()

		self.m_pos = (-10,-10)    #Mouse Coordinates
		self.m_down = False	#Left Mouse Button Down
		self.m_pos_down = (-10,-10)  #Mouse Down Coordinates

		self.grid = Board(22,18,(1,0))  #Board
		self.thing = ThingSprite(100)
		
		self.select_T = None	#Tower Selected

		self.T_list = [] #Towers on Grid
		self.tgroup = pygame.sprite.Group()
		
		self.bgroup = pygame.sprite.Group()
		self.gameoptions = pygame.sprite.Group()
		self.pauseoptions = pygame.sprite.Group()
		
		self.vgroup = []
		
		self.allsprite = pygame.sprite.Group()
		self.allsprite.add(self.thing)
		
		self.status = "prep"	#"prep" or "wave"
		self.preptime = 5
		self.wavetime = 20
		self.timer = time()

		self.resource = ATP() #resource
		self.trivia = trivia()
		
		self.wave = 0
		self.currWave = -1
		self.wFont = pygame.font.Font('res/DS-DIGI.TTF', 30)
		self.wSurf = self.wFont.render(str(self.wave), True, (189,0,0))
		self.wRect = self.wSurf.get_rect()
		self.wRect.topleft = (730-self.wRect.centerx),463

		
		self.vplayer = virusAI.Player(self.grid, self.thing, self.tgroup, self.values, self.resource)
		self.fgroup = pygame.sprite.Group()
		self.fgroup.add(self.resource, self.trivia)
		
		self.pgroup = pygame.sprite.Group()

		self.go = False
		
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
					for b in self.gameoptions:
						b.click()
						
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.pause()

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
					self.vgroup.append(self.vplayer.force())

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

				if event.key == K_g:
					self.go = True

				if event.key == K_h:
					with file('ssfile.ss', "wb") as f:
						ss = SaveState()
						ss.save(self.grid.board, self.T_list, self.wave, self.resource.currentATP, self.resource.currentVirusATP)
						pickle.dump(ss, f)

				if event.key == K_j:
					with open('ssfile.ss', 'rb') as f:
    						ss = pickle.load(f)
						self.grid = ss.grid
						for i in ss.tower_list:
							self.T_list.append(i)
						self.wave = wave
						self.resource.currentATP = ss.atp
						self.resource.currentVirusATP = ss.virus_atp
					
	def hasVirus(self):
		v = False
		for g in self.vgroup:
			if g.hasViruses():
				v = True
				break
		return v
		
	def foo(self):
		pass
		
	def pause(self):
		self.pimage = pygame.image.load('res/pausemenu.png')
		self.pimageRect = self.pimage.get_rect()
		
		goagain = Button(pygame.Surface((235,47)).convert(),(400,376),self.foo, 'res/presume.png')
		goquit = Button(pygame.Surface((225,44)).convert(),(400,467),self.foo, 'res/return.png')	
		self.pauseoptions.add(goagain,goquit)

		while(True):
			for event in pygame.event.get():
				if event.type == QUIT:
					self.quit = True
					return
				elif event.type == KEYDOWN:
					if event.key == K_p or event.key == K_ESCAPE:
						return
				elif event.type == MOUSEBUTTONDOWN:
					for sprite in self.pauseoptions:
						c = sprite.click()
						if(c and sprite == goagain):
							return
						elif c and sprite == goquit:
							self.running = False
							return
							
			self.checkEvents()
			self.screen.blit(self.pimage, self.pimageRect)
			self.pauseoptions.update()
			self.pauseoptions.draw(self.screen)
			pygame.display.flip()		
			
	def stop(self):
		self.running = False
	
	def waveg(self):
		self.go = True
	
	def spawnstem(self):
		if self.select_T == None:
			self.select_T = StemCell()
		else:
			self.select_T = None	
	
	def placeTower(self, pos):
		pass
	
	def start(self):
		pause = Button(pygame.Surface((104,20)).convert(),(730,32),self.pause, 'res/pauseg.PNG')
		buy = Button(pygame.Surface((69,20)).convert(),(730,70),self.spawnstem, 'res/buyg.png')
		waveb = Button(pygame.Surface((93,26)).convert(),(730,458),self.waveg, 'res/wave.PNG')
		
		self.gameoptions.add(pause,buy,waveb)
		#self.towerai.getActions()
		while(self.running and not self.thing.isDead()):
			print self.testing
			self.clock.tick(60)
			self.checkEvents()
			if self.wave == 11 and self.testing == True:
				self.running = False
			#print 'currWave:', self.currWave, 'wave:', self.wave, 'hasVirus:', self.hasVirus()
			
			if self.status == "prep":
				if time() - self.timer >= self.preptime and self.go:
					#WAVE
					self.timer = time()
					self.status = "wave"
					self.vgroup.append(self.vplayer.getNextGroup(self.wave))
					self.go = False
					self.wave += 1
			else:
				if time() - self.timer >= self.wavetime or not self.hasVirus():	#or if no virus exist
					self.timer = time()
					self.status = "prep"
					print "prep"
					self.resource.addATP(self.wave)
					self.resource.addVirusATP(self.wave)
			
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
						gr = self.grid.copy()
						bl = False
						for i in boxContain:
							gr.set(i[0], i[1], 1)
							if not self.vplayer.hasValidPath(gr):
								print "Blocking"
								bl = True
								break
						if self.resource.currentATP - self.select_T.cost >= 0 and not bl:
							self.select_T.setOccupy(boxContain)

							for i in boxContain:
								self.grid.set(i[0],i[1],1)

							self.T_list.append(self.select_T)
							self.tgroup.add(self.select_T) 
							self.resource.currentATP -= self.select_T.cost
							if self.select_T.tower_type == "Stem Cell":
								mods = pygame.key.get_mods()
								if mods & KMOD_LSHIFT:
									print "Yes"
									self.select_T = StemCell()
								else:
									self.select_T = None
							else:
								self.select_T = None
						else:
							if not bl: print 'Not enough ATP'
					else:
						print 'Overlap/Outside Error'

					self.m_down = False
			else:
				if self.m_down:

					#Check if PopUp is being clicked
					for i in self.pgroup:
						if i.prevRect.collidepoint(self.m_pos_down[0], self.m_pos_down[1]):
							print 'prev'
							i.prev()
							self.m_pos_down = -10, -10
						if i.nextRect.collidepoint(self.m_pos_down[0], self.m_pos_down[1]):
							print 'next'
							i.next()
							self.m_pos_down = -10, -10
						if i.sellRect.collidepoint(self.m_pos_down[0], self.m_pos_down[1]):
							print 'sell'							
							self.resource.currentATP += i.tower.cost
							i.sell()
							self.m_pos_down = -10, -10
						if i.upgradeRect != None and i.upgradeRect.collidepoint(self.m_pos_down[0], self.m_pos_down[1]):
							print 'upgrade'
							if i.upgrade().cost <= self.resource.currentATP:
								i.sell()
								self.select_T = i.upgrade()
							else:
								print 'Not enough ATP'
							self.m_pos_down = -10, -10

					#Check if Tower is being clicked
					for i in self.T_list:
						for j in i.occupy:
							if j == self.grid.coorToIndex(self.m_pos_down, i.size):
								if i.view_atk:								
									i.view_atk = False
									i.view_upgrade.visible = False
									i.view_upgrade = None
								else:
									if i.view_upgrade == None:
										pop = PopUp(self.m_pos_down[0],self.m_pos_down[1], i)
										i.view_atk = True
										i.view_upgrade = pop									
										self.pgroup.add(pop)								
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
								if not i.visible and j.tower_type != 'T-Cell': continue
								j.Shoot(i,self.bgroup)
								shoot = True
								break
					if shoot: break
				if j.tower_type == 'Neutrophil':
					j.Shoot(vlist, self.bgroup)

			#Removes Tower from T_List and sets occupy in Grid to 0
			for i in self.T_list:
				present = False
				for j in self.tgroup:
					if j == i:
						present = True
				if present == False:
					for k in i.occupy:
						self.grid.set(k[0],k[1],0)
					self.T_list.remove(i)

			for i in self.vgroup:
				for j in i:
					print j.life, 
			print '\n'

			self.tgroup.update()
			self.tgroup.draw(self.screen)

			self.fgroup.update()
			self.fgroup.draw(self.screen)

			#Display PopUp
			self.pgroup.update()
			self.pgroup.draw(self.screen)

			#display wave
			self.wSurf = self.wFont.render(str(self.wave), True, (189,0,0))
			self.wRect = self.wSurf.get_rect()
			self.wRect.topleft = (730-self.wRect.centerx),463
			self.screen.blit(self.wSurf, self.wRect)
			
			self.gameoptions.update()
			self.gameoptions.draw(self.screen)
	
			pygame.display.update()
			
		return self.wave, self.thing.life
  
class Mainmenu:

	def __init__(self, screen):
		self.screen = screen
		self.running = True
		self.bg = pygame.Surface((800, 600)) #temporary BG
		self.bg = self.bg.convert()
		self.mainoptions = pygame.sprite.Group()
		self.image = pygame.image.load('res/mainmenu.png')
		self.imageRect = self.image.get_rect()

		self.m_pos = (-10,-10)    #Mouse Coordinates
		self.m_down = False	#Left Mouse Button Down
		self.m_pos_down = (-10,-10)  #Mouse Down Coordinates
		self.allsprite = pygame.sprite.Group()

		self.bgm = pygame.mixer.Sound('res//bgm.ogg')
		self.creditoptions = pygame.sprite.Group()		
		self.helpoptions = pygame.sprite.Group()		
		
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
					for b in self.mainoptions:
						b.click()

			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.running = False

	def foo(self):
		pass
					
	def stop(self):
		self.running = False
	
	def startgame(self):
		game = Game(self.screen)
		game.start() 
		
		if game.thing.isDead():
			while(True):
				g = Gameover(self.screen)
				action = g.start()
				if action == 'again':
					game.reinitialize()
					game.start()
				else: break
		pygame.event.get()
	
	def credits(self):
		self.pimage = pygame.image.load('res/creditsmenu.png')
		self.pimageRect = self.pimage.get_rect()
		
		goquit = Button(pygame.Surface((225,44)).convert(),(670,544),self.foo, 'res/return.png')	
		self.creditoptions.add(goquit)

		while(True):
			for event in pygame.event.get():
				if event.type == QUIT:
					self.quit = True
					return
				elif event.type == KEYDOWN:
					if event.key == K_p or event.key == K_ESCAPE:
						return
				elif event.type == MOUSEBUTTONDOWN:
					for sprite in self.creditoptions:
						c = sprite.click()
						if(c and sprite == goquit):
							return

							
			self.checkEvents()
			self.screen.blit(self.pimage, self.pimageRect)
			self.creditoptions.update()
			self.creditoptions.draw(self.screen)
			pygame.display.flip()		

	def help(self):
		self.pimage = pygame.image.load('res/helpmenu.png')
		self.pimageRect = self.pimage.get_rect()
		
		self.page = 1
		
		goquit = Button(pygame.Surface((225,44)).convert(),(670,544),self.foo, 'res/return.png')	
		gonext = Button(pygame.Surface((146,44)).convert(),(468,543),self.foo, 'res/next.PNG')	
		self.helpoptions.add(goquit,gonext)

		while(True):
			for event in pygame.event.get():
				if event.type == QUIT:
					self.quit = True
					return
				elif event.type == KEYDOWN:
					if event.key == K_p or event.key == K_ESCAPE:
						return
				elif event.type == MOUSEBUTTONDOWN:
					for sprite in self.helpoptions:
						c = sprite.click()
						if(c and sprite == goquit):
							return
						elif c and sprite == gonext:
							if self.page == 1:
								self.pimage = pygame.image.load('res/helpmenu2.png')
								self.page = 2
							elif self.page == 2:
								self.pimage = pygame.image.load('res/helpmenu.png')
								self.page = 1
							
			self.checkEvents()
			self.screen.blit(self.pimage, self.pimageRect)
			self.helpoptions.update()
			self.helpoptions.draw(self.screen)
			pygame.display.flip()		
			
	
	def start(self):
		

		start = Button(pygame.Surface((190,43)).convert(),(315,379),self.startgame , 'res/start.PNG')
		help = Button(pygame.Surface((143,43)).convert(),(508,379),self.help, 'res/help.PNG')
		credits = Button(pygame.Surface((244,41)).convert(),(308,469),self.credits, 'res/credits.PNG')
		quit = Button(pygame.Surface((153,41)).convert(),(537,468),self.stop , 'res/quit.PNG')
		self.mainoptions.add(start,help,credits,quit)
		
		self.bgm.play(-1)
		while(self.running):
			self.checkEvents()
			self.screen.blit(self.bg, (0, 0))
			self.screen.blit(self.image, self.imageRect)
			self.allsprite.update()
			self.allsprite.draw(self.screen)
			self.mainoptions.update()
			self.mainoptions.draw(self.screen)
			pygame.display.update()
		self.bgm.stop()
class Gameover:

	def __init__(self, screen):
		self.screen = screen
		self.running = True
		self.bg = pygame.Surface((800, 600)) #temporary BG
		self.bg = self.bg.convert()
		self.overoptions = pygame.sprite.Group()
		self.image = pygame.image.load('res/gameover.png')
		self.imageRect = self.image.get_rect()

		self.allsprite = pygame.sprite.Group()
		self.action = None
			
	def checkEvents(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.running = False

			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					print 'left mouse button'
					self.m_down = True
					self.m_pos_down = (event.pos[0], event.pos[1])
					for b in self.overoptions:
						b.click()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.running = False
					
	def stop(self, action):
		self.running = False
		self.action = action
					
	def start(self):

		goagain = Button(pygame.Surface((341,47)).convert(),(400,376),lambda: self.stop('again'), 'res/goagain.png')
		goquit = Button(pygame.Surface((225,44)).convert(),(400,467),lambda: self.stop('return'), 'res/goreturn.png')
		self.overoptions.add(goagain,goquit)

		while(self.running):
			self.checkEvents()
			self.screen.blit(self.bg, (0, 0))
			self.screen.blit(self.image, self.imageRect)
			self.allsprite.update()
			self.allsprite.draw(self.screen)
			self.overoptions.update()
			self.overoptions.draw(self.screen)
			pygame.display.update()
  
		return self.action

  
if __name__ == '__main__':	

	pygame.init()
	pygame.display.set_caption("Heart Attack")
	icon = pygame.image.load('res/icon.png')
	pygame.display.set_icon(icon)
	SCREEN = pygame.display.set_mode((800, 600))
	#pygame.display.toggle_fullscreen()
	

	mmenu = Mainmenu(SCREEN)
	mmenu.start()
	





















