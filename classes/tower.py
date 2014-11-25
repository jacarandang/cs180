import pygame

class Tower(pygame.sprite.Sprite):

	def __init__(self, w=1, h=1, size=30, damage=1, tower_type='nml'):
		pygame.sprite.Sprite.__init__(self)
		self.damage = damage
		self.w = w
		self.h = h
		self.size = size
		self.tower_type = tower_type

		self.image = pygame.Surface([self.w, self.h])
		self.image.fill((0,0,0))

		self.rect = self.image.get_rect()

		self.occupy = []

	def drawBox(self, x_o=0, y_o=0, screen=None):
		y = y_o + self.occupy[0][1]*self.size
		for i in range(self.h):
			x = x_o + self.occupy[0][0]*self.size
			for j in range(self.w):
				pygame.draw.rect(screen,(0,0,255),(x, y, self.size, self.size), 0)
				x += self.size
			y += self.size
