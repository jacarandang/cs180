import pygame
from pygame.locals import *

class ATP(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.initATP = 30
		self.currentATP = self.initATP
		self.basicFont = pygame.font.SysFont(None, 30)
		self.displayText = str(self.currentATP)
		self.image = self.basicFont.render(self.displayText, True, (255,255,255))
		self.rect = self.image.get_rect()
		self.rect.topleft = 675,490
		
	def addATP(self, wave):
		#FUNCTION: ((0.3x)^2)+15
		self.currentATP += int((0.3*wave)**2)+15

	def update(self):
		self.displayText = str(self.currentATP)
		self.image = self.basicFont.render(self.displayText, True, (255,255,255))
	

