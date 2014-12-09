import pygame
import random
from pygame.locals import *
from base import VirusBase, VirusGroupBase
from time import time

#An Individual Virus Sprite
class VirusSprite(VirusBase, pygame.sprite.Sprite):
	
	def __init__(self, board, thing, life = 10, speed = 10, name = "", cost = 1, resource = None):
		pygame.sprite.Sprite.__init__(self)
		VirusBase.__init__(self, board, life, speed)
		self.size = 30
		
		self.image = pygame.Surface((self.size, self.size))
		#pygame.draw.circle(self.image, (255, 0, 0), (15, 15), 15)
		pygame.draw.circle(self.image, (0,0,0), (15,15), 15)
		self.image.set_colorkey((0, 0, 0), RLEACCEL)
		
		self.name = name
		self.thing = thing
		self.radius = 15
		self.rect = self.image.get_rect()
		self.pos = (-self.size, -self.size)
		self.rect.topleft = self.pos
		self.time = time()

		self.dps = 0 #Ticks of DPS
		self.dpsTimer = time()
		self.dpsDmg = 0

		self.atime = time() #attack timer

		self.multiplier = 1 #Dmg Multiplier
		self.utime = time() #update timer
		self.stuntime = 0
		self.timestunned = 0
		
		self.resource = resource
		
		if random.randint(1,100) <= 5:
			self.visible = False
			self.inviPast = True
		else:
			self.visible = True
			self.inviPast = False
		
		self.initiated = False
		
		self.cost = cost
	def init(self):
		#Initiate the virus(display on screen)
		self.x, self.y = 0, 0 
		if self.getCurrentAction() != None:
			self.x, self.y = self.getCurrentAction()
		self.pos = self.x*self.size, self.y*self.size
		self.step = 0
		self.rect.topleft = self.pos
		self.time = time()
		self.utime = time()
		self.atime = time()
		self.initiated = True
		
	def update(self):
		if not self.initiated: return
		#update function, automatically called by pygame.sprite.Group

		if self.visible == False:
			self.image = pygame.Surface((self.size, self.size))
			pygame.draw.circle(self.image, (0,0,0), (15,15), 15)
			self.image.set_colorkey((0, 0, 0), RLEACCEL)
		elif self.inviPast and self.visible:
			self.reappear()

		dpsDiff = time() - self.dpsTimer
		if dpsDiff >= 0.25:
			self.life = self.life - self.dpsDmg*self.multiplier
			self.dps -= 1
			self.dpsTimer = time()
		
		if self.dps == 0:
			self.dpsTimer = time()
			self.dpsDmg = 0

		dt = time() - self.utime
		self.utime = time()
		
		if self.life <= 0:
			self.kill()
			self.resource.currentATP += 1
			
		if self.x == self.board.w - 1:
			if time() - self.atime >= self.rod:
				self.atime = time()
				self.thing.damage(self.dmg)
				self.resource.currentVirusATP += 1
			return
		diff = time() - self.time - self.timestunned
		
		if self.stuntime > 0:
			self.stuntime -= dt
			self.timestunned += dt
			if self.stuntime <= 0: self.stuntime = 0
			return
		
		if diff  >= 1.00/self.speed:
			self.time = time()
			self.timestunned = 0
			self.setNextAction()
			x, y = self.getCurrentAction()
			self.pos = x*self.size, y*self.size
			self.rect.topleft = self.pos
			if self.getCurrentAction() is None: return
			self.x, self.y = self.getCurrentAction()
		else:
			target = self.getNextAction()
			if(target == None): return
			dx = (target[0] - self.x) * dt * self.speed * self.size
			dy = (target[1] - self.y) * dt * self.speed * self.size
			self.pos = self.pos[0] + dx , self.pos[1] + dy
		self.rect.topleft = self.pos

	def stun(self, time):
		self.stuntime += time

	def reappear(self):
		pass

	def __repr__(self):
		return self.name
		
#A Virus Group which also serves as a Sprite Group		
class VirusGroup(pygame.sprite.Group, VirusGroupBase):

	def __init__(self, *viruses):
		self.hvirus = [i for i in viruses]
		pygame.sprite.Group.__init__(self)
		VirusGroupBase.__init__(self)
		self.timer = time()
			
	def add(self, *viruses):
		for v in viruses:
			self.hvirus.append(v)
			
	def addToGroup(self, *viruses):
		pygame.sprite.Group.add(self, *viruses)
		VirusGroupBase.add(self, *viruses)

	def update(self):
		if time() - self.timer >= 0.25:
			self.timer = time()
			if not len(self.hvirus) == 0:
				v = self.hvirus.pop()
				self.addToGroup(v)
				v.init()
		pygame.sprite.Group.update(self)
		
	def hasViruses(self):
		return len(self.hvirus) != 0 or len(pygame.sprite.Group.sprites(self)) != 0
		
class Fungi(VirusSprite):

	def __init__(self, board, thing, res):
		VirusSprite.__init__(self, board, thing, 10, 10, "fungi", 1, res)
		self.image = pygame.image.load('res/fungi.png').convert_alpha()
		self.visibleImage = self.image
		self.rect = self.image.get_rect()
		self.rect.topleft = (-30, -30)

	def reappear(self):
		self.image = pygame.image.load('res/fungi.png').convert_alpha()
		self.visibleImage = self.image
		self.rect = self.image.get_rect()
		self.rect.topleft = self.pos
		
class Parasite(VirusSprite):

	def __init__(self, board, thing, res):
		VirusSprite.__init__(self, board, thing, 20, 2.5, "parasite", 5, res)
		self.images = []
		for i in xrange(1, 9):
			
			self.images.append(pygame.image.load('res/parasite'+str(i)+'.png'))
		self.image = self.images[0]
		self.iidx = 0
		self.animtime = time()
		self.rect = self.image.get_rect()
		self.rect.topleft = (-30, -30)
		
	def update(self):
		VirusSprite.update(self)
		if time() - self.animtime > 1/self.speed*1.00:
			self.animtime = time()
			self.iidx += 1
			self.iidx %= 8
			self.image = self.images[self.iidx]

	def reappear(self):
		self.images = []
		for i in xrange(1, 9):
			self.images.append(pygame.image.load('res/parasite'+str(i)+'.png'))
		self.image = self.images[0]
		self.iidx = 0
		self.animtime = time()
		self.rect = self.image.get_rect()
		self.rect.topleft = self.pos
			
class Bacteria(VirusSprite):

	def __init__(self, board, thing, res):
		VirusSprite.__init__(self, board, thing, 80, 6, "bacteria", 10, res)
		self.image = pygame.image.load('res/bacteria.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topleft = (-30, -30)
		
class Virus(VirusSprite):

	def __init__(self, board, thing, res):
		VirusSprite.__init__(self, board, thing, 50, 8, "virus", 7, res)
		self.image = pygame.image.load('res/virus.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topleft = (-30, -30)

	def reappear(self):
		self.image = pygame.image.load('res/virus.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topleft = self.pos
		
class Ebola(VirusSprite):

	def __init__(self, board, thing, res):
		VirusSprite.__init__(self, board, thing, 40, 8, "ebola", 10, res)
		self.images = []
		for i in xrange(1, 9):
			self.images.append(pygame.image.load('res/ebola'+str(i)+'.png'))
		self.image = self.images[0]
		self.iidx = 0
		self.animtime = time()
		self.rect = self.image.get_rect()
		self.rect.topleft = self.pos
		self.rect.topleft = (-30, -30)
		
	def update(self):
		VirusSprite.update(self)
		if time() - self.animtime > 1/self.speed*1.00:
			self.animtime = time()
			self.iidx += 1
			self.iidx %= 8
			self.image = self.images[self.iidx]

	def reappear(self):
		self.images = []
		for i in xrange(1, 9):
			self.images.append(pygame.image.load('res/ebola'+str(i)+'.png'))
		self.image = self.images[0]
		self.iidx = 0
		self.animtime = time()
		self.rect = self.image.get_rect()
		self.rect.topleft = self.pos
			
class HIV(VirusSprite):

	def __init__(self, board, thing, res):
		VirusSprite.__init__(self, board, thing, 80, 4, "hiv", 20, res)
		self.image = pygame.image.load('res/hiv.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topleft = (-30, -30)

	def reappear(self):
		self.image = pygame.image.load('res/hiv.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topleft = self.pos
