import pygame
from pygame.locals import *
from base import VirusBase

class Virus(VirusBase, pygame.sprite.Sprite):
	
	def __init__(self, life = 10, speed = 1, board = None, size = 30):
		pygame.sprite.Sprite.__init__(self)
		VirusBase.__init__(self, life, speed, board)
		self.size = size
		self.image = pygame.Surface((self.size, self.size))
		self.rect = self.image.get_rect()
		
	def update():
		pass
	