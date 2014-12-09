import pygame
from pygame.locals import *
import random
from time import time

class trivia(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.t = [
		"Virus was coined from the Latin word meaning poison",
		"Bacteria was coined from the Greek 'bakterion' word meaning small rod or staff",
		"Walter Reed discovered the first human virus, yellow fever, in 1901",
		"Bacteria are single-celled microorganisms that thrive in different environments",
		"Viruses are even smaller than bacteria and require living hosts to multiply",
		"The current Ebola outbreak is most widespread and intense in West Africa",
		"There are more than 100 different viruses that cause the common cold",
		"Ebola virus is passed from person to person via bodily fluids",
		"Early Ebola symptoms are also symptoms of other viral infections",
		"5177 deaths were reported due to Ebola as of Nov 14",
		"Bleeding is common in the later stages of Ebola",
		"ZMapp is an experimental medication in development to fight ebola",
		"HIV (human immunodeficiency virus) infects cells of the immune system",
		"35 million people are living with HIV worldwide",
		"HIV is the world's leading infectious killer, with 39 million deaths"
		]
		self.basicFont = pygame.font.Font('res/UltraCondensedSansSerif.ttf', 30)
		self.displayText = random.choice(self.t)
		self.image = self.basicFont.render(self.displayText, True, (189,0,0))
		self.rect = self.image.get_rect()
		self.rect.topleft = (400-self.rect.centerx),553
		self.time = time()
		
	def update(self):
		if time() - self.time >= 10:
			self.displayText = random.choice(self.t)
			self.image = self.basicFont.render(self.displayText, True, (189,0,0))
			self.rect = self.image.get_rect()
			self.rect.topleft = (400-self.rect.centerx),553
			self.time = time()
			