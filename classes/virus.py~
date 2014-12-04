import pygame
from pygame.locals import *
from base import VirusBase
from time import time

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
		
	def init(self):
		self.x, self.y = self.getCurrentAction()
		self.pos = self.x*self.size, self.y*self.size
		self.pos.topleft = self.pos
		self.time = time()
		
	def update(self):
		diff = time() - self.time
		if diff >= 1.00/self.speed:
			self.time = time()
			self.setNextAction()

			if self.getCurrentAction() != None:
				self.x, self.y = self.getCurrentAction()
		else:
			target = self.getNextAction()
			if(target == None): return
			dx = (target[0] - self.x) * diff * self.speed * self.size
			dy = (target[1] - self.y) * diff * self.speed * self.size
			self.pos = self.x*30 + dx, self.y*30 + dy

		self.rect.topleft = self.pos
