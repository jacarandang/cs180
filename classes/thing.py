import pygame
from pygame.locals import *
from base import Thing

class ThingSprite(pygame.sprite.Sprite, Thing):

	def __init__(self, life):
		Thing.__init__(self, life)
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('res/hpgrid.PNG')
		self.rect = self.image.get_rect()
		self.top = 100
		self.height = 345
		self.y = self.top
		self.rect.topleft = 0, 100
		
	def update(self):
		p = self.percentage()
		self.y = self.top + (1-p)*self.height
		self.rect.top = self.y