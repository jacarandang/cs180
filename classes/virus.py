import pygame
from pygame.locals import *
from base import VirusBase, VirusGroupBase
from time import time

#An Individual Virus Sprite
class VirusSprite(VirusBase, pygame.sprite.Sprite):
	
	def __init__(self, board, thing, life = 10, speed = 10):
		pygame.sprite.Sprite.__init__(self)
		VirusBase.__init__(self, board, life, speed)
		self.size = 30
		
		self.image = pygame.Surface((self.size, self.size))
		pygame.draw.circle(self.image, (255, 0, 0), (15, 15), 15)
		self.image.set_colorkey((0, 0, 0), RLEACCEL)
		
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
		
	def init(self):
		#Initiate the virus(display on screen)
		self.x, self.y = self.getCurrentAction()
		self.pos = self.x*self.size, self.y*self.size
		self.pos.topleft = self.pos
		self.time = time()
		
	def update(self):
		#update function, automatically called by pygame.sprite.Group
		dpsDiff = time() - self.dpsTimer
		if dpsDiff >= 0.25:
			self.life = self.life - self.dpsDmg 
			self.dps -= 1
			self.dpsTimer = time()
		
		if self.dps == 0:
			self.dpsTimer = time()
			self.dpsDmg = 0

		if self.life <= 0:
			self.kill()
		if self.x == self.board.w - 1:
			if time() - self.atime >= self.rod:
				self.atime = time()
				self.thing.damage(self.dmg)
				
		diff = time() - self.time
		if diff >= 1.00/self.speed:
			self.time = time()
			self.setNextAction()
			if self.getCurrentAction() is None: return
			self.x, self.y = self.getCurrentAction()
		else:
			target = self.getNextAction()
			if(target == None): return
			dx = (target[0] - self.x) * diff * self.speed * self.size
			dy = (target[1] - self.y) * diff * self.speed * self.size
			self.pos = self.x*30 + dx, self.y*30 + dy

		self.rect.topleft = self.pos

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
		VirusSprite.__init__(self, board, thing, 20, 10)
		self.image = pygame.image.load('res/fungi.png').convert_alpha()
		self.rect = self.image.get_rect()
		
class Parasite(VirusSprite):

	def __init__(self, board, thing):
		VirusSprite.__init__(self, board, thing, 100, 2.5)
		self.image = pygame.image.load('res/parasite1.png').convert_alpha()
		self.rect = self.image.get_rect()
		
class Bacteria(VirusSprite):

	def __init__(self, board, thing):
		VirusSprite.__init__(self, board, thing, 60, 6)
		self.image = pygame.image.load('res/bacteria.png').convert_alpha()
		self.rect = self.image.get_rect()
		
class Virus(VirusSprite):

	def __init__(self, board, thing):
		VirusSprite.__init__(self, board, thing, 60, 8)
		self.image = pygame.image.load('res/virus.png').convert_alpha()
		self.rect = self.image.get_rect()
		
class Ebola(VirusSprite):

	def __init__(self, board, thing):
		VirusSprite.__init__(self, board, thing, 20, 8)
		self.image = pygame.image.load('res/ebola1.png').convert_alpha()
		self.rect = self.image.get_rect()
		
class HIV(VirusSprite):

	def __init__(self, board, thing):
		VirusSprite.__init__(self, board, thing, 90, 4)
		self.image = pygame.image.load('res/hiv.png').convert_alpha()
		self.rect = self.image.get_rect()
