import pygame
from pygame.locals import *

class ATP(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#Tower ATP
		self.initATP = 50
		self.currentATP = self.initATP

		#Virus ATP
		self.initVirusATP = 30
		self.currentVirusATP = self.initVirusATP
		
		self.basicFont = pygame.font.Font('res/DS-DIGI.TTF', 30)
		self.displayText = str(self.currentATP)
		self.image = self.basicFont.render(self.displayText, True, (189,0,0))
		self.rect = self.image.get_rect()
		self.rect.topleft = (730-self.rect.centerx),511
		
	def addATP(self, wave):
		#FUNCTION: ((0.3x)^2)+15
		self.currentATP += int((0.3*wave)**2)+15

	def addVirusATP(self, wave):
		#FUNCTION:
		self.currentVirusATP += 30 + 5*wave
		print self.currentVirusATP

	def update(self):
		self.displayText = str(self.currentATP)
		self.image = self.basicFont.render(self.displayText, True, (189,0,0))
		self.rect = self.image.get_rect()
		self.rect.topleft = (730-self.rect.centerx),511

