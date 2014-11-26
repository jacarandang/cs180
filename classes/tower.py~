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

		self.atk_range = (w+2, h+2)
		self.atk_pos = []

		self.view_atk = False

	def setOccupy(self, boxContain):
		for i in boxContain:
			self.occupy.append(i)

		y = self.occupy[0][1]-1
		for i in range(self.atk_range[1]):
			x = self.occupy[0][0]-1
			for j in range(self.atk_range[0]):
				self.atk_pos.append((x+j,y+i))

	def drawBox(self, x_o=0, y_o=0, screen=None):
		y = y_o + self.occupy[0][1]*self.size
		for i in range(self.h):
			x = x_o + self.occupy[0][0]*self.size
			for j in range(self.w):
				pygame.draw.rect(screen,(0,0,255),(x, y, self.size, self.size), 0)
				x += self.size
			y += self.size

	def drawAtk(self, x_o=0, y_o=0, screen=None):
		y = y_o + (self.atk_pos[0][1])*self.size
		for i in range(self.atk_range[1]):
			x = x_o + (self.atk_pos[0][0])*self.size
			for j in range(self.atk_range[0]):
				pygame.draw.rect(screen, (102,0,102), (x,y,self.size, self.size), 0)
				x += self.size
			y += self.size

