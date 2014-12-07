import pygame
from pygame.locals import *

class bullet(pygame.sprite.Sprite):
	def __init__(self, x=0, y=0, speed=5, dmg=1,virus=None):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.speed = 1.00/60
		self.dmg = dmg
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
			dx = 5
			dy = 5
			if self.virus.pos[0] - self.x > 0:
				self.x = self.x + dx
			else:
				self.x = self.x - dx

			if self.virus.pos[1] - self.y > 0:
				self.y = self.y + dy			
			else:
				self.y = self.y - dy
			self.rect.topleft = self.x, self.y
		else:
			self.virus.life = self.virus.life - self.dmg*self.virus.multiplier
			self.kill()


class DPSbullet(bullet):
	def __init__(self, x=0, y=0, speed=5, dmg=1,virus=None, dps=10):
		bullet.__init__(self, x, y, speed, dmg,virus)

		self.dps = dps

	def update(self):
		if not pygame.sprite.collide_circle(self, self.virus):
			dx = 5
			dy = 5
			if self.virus.pos[0] - self.x > 0:
				self.x = self.x + dx
			else:
				self.x = self.x - dx

			if self.virus.pos[1] - self.y > 0:
				self.y = self.y + dy			
			else:
				self.y = self.y - dy
			self.rect.topleft = self.x, self.y
		else:
			#Damage over time
			self.virus.dps = self.dps
			self.virus.dpsDmg = self.dmg
			self.kill()

class TagBullet(bullet):
	def __init__(self, x=0, y=0, speed=5, dmg=1,virus=None, mult=2):
		bullet.__init__(self, x, y, speed, dmg, virus)

		self.mult = mult

	def update(self):
		if not pygame.sprite.collide_circle(self, self.virus):
			dx = 5
			dy = 5
			if self.virus.pos[0] - self.x > 0:
				self.x = self.x + dx
			else:
				self.x = self.x - dx

			if self.virus.pos[1] - self.y > 0:
				self.y = self.y + dy			
			else:
				self.y = self.y - dy
			self.rect.topleft = self.x, self.y
		else:
			#Damage multiplier 
			self.virus.multiplier = self.virus.multiplier + self.mult
			self.kill()

class DetectBullet(bullet):
	def __init__(self, x=0, y=0, speed=5, dmg=1,virus=None):
		bullet.__init__(self, x, y, speed, dmg, virus)
		
	def update(self):
		if not pygame.sprite.collide_circle(self, self.virus):
			dx = 5
			dy = 5
			if self.virus.pos[0] - self.x > 0:
				self.x = self.x + dx
			else:
				self.x = self.x - dx

			if self.virus.pos[1] - self.y > 0:
				self.y = self.y + dy			
			else:
				self.y = self.y - dy
			self.rect.topleft = self.x, self.y
		else:
			#Detect Virus
			if self.virus.visible == False:
				self.virus.visible = True
			self.virus.life = self.virus.life - self.dmg*self.virus.multiplier
			self.kill()
		
