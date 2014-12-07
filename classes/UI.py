import pygame
from pygame.locals import *

class HoverDown(pygame.sprite.Sprite):

	#args, width, height size of hover
	#x, y coordinates when shown
	#dir direction when transitioning from hidden to shown state
	#0 - up, 1 - right, 2 - down, 3 - left
	#remaining pixel not shown
	def __init__(self, w, h, x, y, dir, rem = 10):
		pygame.sprite.Sprite.__init__(self)
		self.w = w
		self.h = h
		self.fx = x
		self.fy = y
		self.dir = dir
		self.rem = rem
		self.toShow = [(0, 1), (-1, 0), (0, -1), (1, 0)]
		self.hx = self.fx - self.toShow[self.dir][0] * -1*self.w	+	self.rem*self.toShow[self.dir][0]
		self.hy =self.fy - self.toShow[self.dir][1] * -1*self.h	+	self.rem*self.toShow[self.dir][1]*-1
		self.image = pygame.Surface((self.w, self.h))
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect()
		
		self.x = self.hx
		self.y = self.hy
		self.rect.topleft = self.hx, self.hy
		
	def update(self):
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			if self.x != self.fx or self.y != self.fy:
				self.x = self.fx
				self.y = self.fy
		else:
			if self.x != self.hx or self.y != self.hy:
				self.x = self.hx
				self.y = self.hy
		self.rect.topleft = self.x, self.y
		
		
class Button(pygame.sprite.Sprite):

	def __init__(self, image, (x, y), action, name, selected = False):
		pygame.sprite.Sprite.__init__(self)
		self.name = name
		self.nimage =  image
		self.nimage.set_colorkey((0, 0, 0), RLEACCEL)
		self.simage = pygame.image.load(name)
		self.nrect = self.nimage.get_rect()
		self.srect = self.simage.get_rect()
		self.srect.w = self.nrect.w 	
		self.image, self.rect = None , None
		if(selected):
			self.image = self.simage
			self.rect = self.srect
		else:
			self.image = self.nimage
			self.rect = self.nrect
		self.action = action
		self.x = x
		self.y = y
		self.rect.center = self.x, self.y

	def update(self):
		if(self.rect.collidepoint(pygame.mouse.get_pos())): #mousehover
			if self.image != self.simage:
				self.image = self.simage
				self.rect = self.srect
				self.rect.center = self.x, self.y
		else:
			if self.image != self.nimage:
				self.image = self.nimage
				self.rect = self.nrect
				self.rect.center = self.x, self.y
			
			
	def click(self):
		if(self.rect.collidepoint(pygame.mouse.get_pos())):
			self.action()
			return True
		return False