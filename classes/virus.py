import pygame
from pygame.locals import *
from base import VirusBase, VirusGroupBase
from time import time

#An Individual Virus Sprite
class VirusSprite(VirusBase, pygame.sprite.Sprite):
	
	def __init__(self, board, thing, life = 10, speed = 10, name = ""):
		pygame.sprite.Sprite.__init__(self)
		VirusBase.__init__(self, board, life, speed)
		self.size = 30
		
		self.image = pygame.Surface((self.size, self.size))
		pygame.draw.circle(self.image, (255, 0, 0), (15, 15), 15)
		self.image.set_colorkey((0, 0, 0), RLEACCEL)
		
		self.name = name
		self.thing = thing
		self.radius = 15
		self.rect = self.image.get_rect()
		self.pos = (-self.size, -self.size)
		self.rect.topleft = self.pos
		self.time = time()
		self.atime = time() #attack timer
		self.utime = time() #update timer
		self.stuntime = 0
		self.timestunned = 0
		
	def init(self):
		#Initiate the virus(display on screen)
		self.x, self.y = self.getCurrentAction()
		self.pos = self.x*self.size, self.y*self.size
		self.rect.topleft = self.pos
		self.time = time()
		
	def update(self):
		#update function, automatically called by pygame.sprite.Group
		dt = time() - self.utime
		self.utime = time()
		
		if self.life <= 0:
			self.kill()
			
		if self.x == self.board.w - 1:
			if time() - self.atime >= self.rod:
				self.atime = time()
				self.thing.damage(self.dmg)
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
		
#A Virus Group which also serves as a Sprite Group		
class VirusGroup(pygame.sprite.Group, VirusGroupBase):

	def __init__(self, *viruses):
		pygame.sprite.Group.__init__(self, *viruses)
		VirusGroupBase.__init__(self)
		for v in viruses:
			VirusGroupBase.add(v)
		
	def add(self, *viruses):
		pygame.sprite.Group.add(self, *viruses)
		VirusGroupBase.add(self, *viruses)

class Fungi(VirusSprite):

	def __init__(self, board, thing):
		VirusSprite.__init__(self, board, thing, 20, 10, "fungi")
		self.image = pygame.image.load('res/fungi.png').convert_alpha()
		self.rect = self.image.get_rect()
		
class Parasite(VirusSprite):

	def __init__(self, board, thing):
		VirusSprite.__init__(self, board, thing, 20, 2.5, "parasite")
		self.images = []
		for i in xrange(1, 6):
			self.images.append(pygame.image.load('res/parasite'+str(i)+'.png'))
		self.image = self.images[0]
		self.iidx = 0
		self.animtime = time()
		self.rect = self.image.get_rect()
		
	def update(self):
		VirusSprite.update(self)
		if time() - self.animtime > 1/self.speed*1.00:
			self.animtime = time()
			self.iidx += 1
			self.iidx %= 5
			self.image = self.images[self.iidx]
			
class Bacteria(VirusSprite):

	def __init__(self, board, thing):
		VirusSprite.__init__(self, board, thing, 60, 6, "bacteria")
		self.image = pygame.image.load('res/bacteria.png').convert_alpha()
		self.rect = self.image.get_rect()
		
class Virus(VirusSprite):

	def __init__(self, board, thing):
		VirusSprite.__init__(self, board, thing, 60, 8, "virus")
		self.image = pygame.image.load('res/virus.png').convert_alpha()
		self.rect = self.image.get_rect()
		
class Ebola(VirusSprite):

	def __init__(self, board, thing):
		VirusSprite.__init__(self, board, thing, 20, 8, "ebola")
		self.images = []
		for i in xrange(1, 6):
			self.images.append(pygame.image.load('res/ebola'+str(i)+'.png'))
		self.image = self.images[0]
		self.iidx = 0
		self.animtime = time()
		self.rect = self.image.get_rect()
		
	def update(self):
		VirusSprite.update(self)
		if time() - self.animtime > 1/self.speed*1.00:
			self.animtime = time()
			self.iidx += 1
			self.iidx %= 5
			self.image = self.images[self.iidx]
			
class HIV(VirusSprite):

	def __init__(self, board, thing):
		VirusSprite.__init__(self, board, thing, 90, 4, "hiv")
		self.image = pygame.image.load('res/hiv.png').convert_alpha()
		self.rect = self.image.get_rect()
