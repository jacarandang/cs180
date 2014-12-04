import pygame
from pygame.locals import *
from base import VirusBase, VirusGroupBase
from time import time

#An Individual Virus Sprite
class Virus(VirusBase, pygame.sprite.Sprite):
	
	def __init__(self, board, life = 10, speed = 10):
		pygame.sprite.Sprite.__init__(self)
		VirusBase.__init__(self, board, life, speed)
		self.size = 30
		
		self.image = pygame.Surface((self.size, self.size))
		pygame.draw.circle(self.image, (255, 0, 0), (15, 15), 15)
		self.image.set_colorkey((0, 0, 0), RLEACCEL)
		
		self.radius = 15
		self.rect = self.image.get_rect()
		self.pos = (-self.size, -self.size)
		self.rect.topleft = self.pos
		self.time = time()
		self.atime = time() #attack timer
		
	def init(self):
		#Initiate the virus(display on screen)
		self.x, self.y = self.getCurrentAction()
		self.pos = self.x*self.size, self.y*self.size
		self.pos.topleft = self.pos
		self.time = time()
		
	def update(self):
		#update function, automatically called by pygame.sprite.Group
		if self.life <= 0:
			self.kill()
		if self.x == self.board.w - 1:
			if time() - self.atime() >= self.rod:
				self.atime = time()
				#damage the thing
				
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
