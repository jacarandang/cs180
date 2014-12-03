import pygame
from pygame.locals import *

class bullet(pygame.sprite.Sprite):
	def __init__(self, x=0, y=0, speed=5, diff=1,virus=None):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.speed = 1.00/60
		self.diff = diff
		self.virus = virus
		self.size = 10

		self.image = pygame.Surface((self.size, self.size))
		pygame.draw.circle(self.image, (255, 255, 0), (self.size/2, self.size/2), self.size/2)
		self.image.set_colorkey((0, 0, 0), RLEACCEL)

		self.rect = self.image.get_rect()
		self.rect.topleft = self.x, self.y
		self.radius = self.size/2

	def update(self):
		if not pygame.sprite.collide_circle(self, self.virus):
			#dx = (self.virus.pos[0] - self.x) * self.diff * self.speed * self.size
			#dy = (self.virus.pos[1] - self.y) * self.diff * self.speed * self.size
			dx = 3
			dy = 3
			if self.virus.pos[0] - self.x > 0:
				self.x = self.x + dx
			else:
				self.x = self.x - dx

			if self.virus.pos[1] - self.y > 0:
				self.y = self.y + dy			
			else:
				self.y = self.y - dy
			self.rect.topleft = self.x, self.y
		