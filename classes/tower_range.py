import pygame
from pygame.locals import *

class tower_range(pygame.sprite.Sprite):
	def __init__(self, rect, radius):
		self.rect = rect
		self.radius = radius
		
