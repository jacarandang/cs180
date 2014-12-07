import pygame
from pygame.locals import *

class ATP(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.initATP = 30
		self.currentATP = self.initATP
		
	def addATP(self, wave):
		#FUNCTION: ((0.3x)^2)+15
		self.currentATP += int((0.3*wave)**2)+15
	

