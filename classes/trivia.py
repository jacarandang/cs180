import pygame
from pygame.locals import *
import random
from time import time

class trivia(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.t = [
		"Virus was coined from the Latin word meaning poison.",
		"Walter Reed discovered the first human virus, yellow fever, in 1901."
		]
		self.basicFont = pygame.font.SysFont(None, 30)
		self.displayText = random.choice(self.t)
		self.image = self.basicFont.render(self.displayText, True, (255,255,255))
		self.rect = self.image.get_rect()
		self.rect.topleft = 9,551
		self.time = time()
		
	def update(self):
		if time() - self.time >= 10:
			self.displayText = random.choice(self.t)
			self.image = self.basicFont.render(self.displayText, True, (255,255,255))
			self.time = time()