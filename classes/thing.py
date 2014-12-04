import pygame
from pygame.locals import *
from base import Thing

class ThingSprite(pygame.sprite.Sprite, Thing):

	def __init__(self, life):
		Thing.__init__(self, life)
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((140, 500)).convert()
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect()
		self.rect.topleft = 640, 0
		
	def update(self):
		pass