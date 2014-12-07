import os, sys
import pygame
from pygame.locals import *
from time import time, sleep
from classes.base import *
from classes.bullet import *
from classes.tower_range import *
from math import sqrt

class Tower(pygame.sprite.Sprite):

	def __init__(self, w=1, h=1, size=30, damage=1, tower_type='nml', shoot=1, cost=1):
		pygame.sprite.Sprite.__init__(self)
		self.damage = damage
		self.w = w
		self.h = h
		self.size = size
		self.tower_type = tower_type
		self.shoot = shoot
		self.cost = cost

		self.image = pygame.Surface([self.w*self.size, self.h*self.size])
		self.image.fill((0,0,0))

		self.rect = self.image.get_rect()

		self.occupy = []

		self.radius = ((self.w+self.h)/2)*30+15
		self.tRange = None

		self.time = time()
		
		self.view_atk = False

	def inRange(self, pos):
		mx = (self.occupy[0][0] + self.occupy[-1][0])/2
		my = (self.occupy[0][1] + self.occupy[-1][1])/2
		return sqrt((mx - pos[0]) ** 2 + (my - pos[1]) **2) <= self.radius/30.00
		
	def __repr__(self):
		return self.tower_type

	def setOccupy(self, boxContain):
		for i in boxContain:
			self.occupy.append(i)

		self.rect.topleft = self.occupy[0][0]*self.size, self.occupy[0][1]*self.size
		self.tRange = tower_range(self.rect, self.radius)

		y = self.occupy[0][1]*self.size
		x = self.occupy[0][0]*self.size
		self.rect.topleft = x, y

	def drawBox(self, x_o=0, y_o=0, screen=None):
		y = y_o + self.occupy[0][1]*self.size
		for i in range(self.h):
			x = x_o + self.occupy[0][0]*self.size
			for j in range(self.w):
				pygame.draw.rect(screen,(0,0,255),(x, y, self.size, self.size), 0)
				x += self.size
			y += self.size

	def drawAtk(self, x_o=0, y_o=0, screen=None):
		pygame.draw.circle(screen,(0,0,0), (self.rect.center), self.radius)
		pass

	def Shoot(self, virus, bulletGroup):
		diff = time() - self.time
		if diff >= 1.00/self.shoot and virus.visible:
			self.time = time()
			bulletGroup.add(bullet(self.rect.center[0], self.rect.center[1], 1, 1, virus))

	def update(self):
		pass


#TOWER ARGUMENTS: (self, w=1, h=1, size=30, damage=1, tower_type='nml', shoot=1, cost=1):

class StemCell(Tower): #Implemented
	def __init__(self):
		Tower.__init__(self, 1, 1, 30, 0, 'Stem Cell', 1, 1)
		
		self.image = pygame.image.load('res/stemcell.PNG')
		self.rect = self.image.get_rect()

	def Shoot(self, virus, bulletGroup):
		pass

class Lymphocyte(Tower): #Implemented
	def __init__(self):
		Tower.__init__(self, 1, 1, 30, 1, 'Lymphocyte', 2, 2)

		self.image = pygame.image.load('res/lymphoid.PNG')
		self.rect = self.image.get_rect()

class NaturalKillerCell(Tower): #Implemented
	#DPS, Poison Damage
	def __init__(self):
		Tower.__init__(self, 2, 2, 30, 2, 'Natural Killer Cell', 1)

		self.image = pygame.image.load('res/natkill.PNG')
		self.rect = self.image.get_rect()

	def Shoot(self, virus, bulletGroup):
		diff = time() - self.time
		if diff >= 1.00/self.shoot and virus.visible:
			self.time = time()
			bulletGroup.add(DPSbullet(self.rect.center[0], self.rect.center[1], 1, 1, virus,10))

class TCell(Tower): #Implemented
	#Weakens Pathogens (Tracks Pathogens if invisible)
	def __init__(self):
		Tower.__init__(self, 2, 2, 30, 2, 'T-Cell', 7)

		self.image = pygame.image.load('res/tcell.PNG')
		self.rect = self.image.get_rect()

	def Shoot(self, virus, bulletGroup):
		diff = time() - self.time
		if diff >= 1.00/self.shoot:
			self.time = time()
			bulletGroup.add(DetectBullet(self.rect.center[0], self.rect.center[1], 1, 1, virus))

class BCell(Tower): #Implemented
	#Increases Damage received of Pathogen (tag based)
	def __init__(self):
		Tower.__init__(self, 2, 2, 30, 2, 'B-Cell', 5)

		self.image = pygame.image.load('res/bcell.PNG')
		self.rect = self.image.get_rect()

	def Shoot(self, virus, bulletGroup):
		diff = time() - self.time
		if diff >= 1.00/self.shoot and virus.visible:
			self.time = time()
			bulletGroup.add(TagBullet(self.rect.center[0], self.rect.center[1], 1, 1, virus,10))

class PlasmaCell(Tower): #Implemented
	#Improved B-Cell, has Damage	
	def __init__(self):
		Tower.__init__(self, 2, 2, 30, 3, 'Plasma Cell', 7)
		
		self.image = pygame.image.load('res/plasma.PNG')
		self.rect = self.image.get_rect()

	def Shoot(self, virus, bulletGroup):
		diff = time() - self.time
		if diff >= 1.00/self.shoot and virus.visible:
			self.time = time()
			bulletGroup.add(TagBullet(self.rect.center[0], self.rect.center[1], 1, 1, virus,10))
			bulletGroup.add(bullet(self.rect.center[0], self.rect.center[1], 1, 1, virus))


class Granulocyte(Tower): #Implemented
	def __init__(self):
		Tower.__init__(self,1, 1, 30, 1, 'Granulocyte', 2, 2)

		self.image = pygame.image.load('res/myeloid.PNG')
		self.rect = self.image.get_rect()

class Basophil(Tower): #Implemented
	#Highly effective against Parasytes and Bacteria, Fast Damage (SMG)
	def __init__(self):
		Tower.__init__(self,1, 1, 30, 2, 'Basophil', 10)

		self.image = pygame.image.load('res/basophil.PNG')
		self.rect = self.image.get_rect()

class Neutrophil(Tower): #Implemented
	#Stuns (engulfs, AOE) and digests enemy Pathogens (small poison damage)
	def __init__(self):
		Tower.__init__(self,2, 2, 30, 2, 'Neutrophil', 2)

		self.image = pygame.image.load('res/neutrophil.PNG')
		self.rect = self.image.get_rect()
		self.stun = self.time

	def Shoot(self, vlist, bulletGroup):
		diffStun = time() - self.stun
		if diffStun >= 3:
			for i in vlist:
				i.stun(1)
			self.stun = time()

		diff = time() - self.time
		if diff >= 1.00/self.shoot:
			for i in vlist:
				if i.visible:
					bulletGroup.add(DPSbullet(self.rect.center[0], self.rect.center[1], 1, 1, i,5))
			self.time = time()

class Eosinophil(Tower): #Implemented
	#Effective against Parasytic and Fungal Pathogens, Fast Damage 
	def __init__(self):
		Tower.__init__(self,1, 1, 30, 2, 'Eosinophil', 10)

		self.image = pygame.image.load('res/eosinophil.PNG')
		self.rect = self.image.get_rect()

class Monocyte(Tower): #Implemented
	#Eats enemies on contact
	def __init__(self):
		Tower.__init__(self,1, 1, 30, 2, 'Monocyte', 0.25)

		self.image = pygame.image.load('res/monocyte.PNG')
		self.rect = self.image.get_rect()

	def Shoot(self, virus, bulletGroup):
		diff = time() - self.time
		if diff >= 1.00/self.shoot and virus.visible:
			self.time = time()
			virus.kill()

class Macrophage(Tower): #Implemented
	#Eats enemies on contact. Better area of effect
	def __init__(self):
		Tower.__init__(self,2, 2, 30, 2, 'Macrophage', 1.5)

		self.image = pygame.image.load('res/macrophage.PNG')
		self.rect = self.image.get_rect()
		self.radius = self.radius*2

	def Shoot(self, virus, bulletGroup):
		diff = time() - self.time
		if diff >= 1.00/self.shoot and virus.visible:
			self.time = time()
			virus.kill()

class Megakaryocyte(Tower): #Implemented
	#Effective against Ebola, can Tank (large HP)
	def __init__(self):
		Tower.__init__(self,3, 3, 30, 2, 'Megakaryocyte', 5)

		self.image = pygame.image.load('res/megakaryocyte.png')
		self.rect = self.image.get_rect()

	def Shoot(self, virus, bulletGroup):
		diff = time() - self.time
		if diff >= 1.00/self.shoot and virus.visible:
			if virus.name == 'ebola':
				bulletGroup.add(bullet(self.rect.center[0], self.rect.center[1], 1, 10, virus))
			else:
				bulletGroup.add(bullet(self.rect.center[0], self.rect.center[1], 1, 5, virus))
			self.time = time()

class Thrombocyte(Tower): #Implemented
	#Improved Megakaryocyte, Highly Effective against Ebola	
	def __init__(self):
		Tower.__init__(self,1, 1, 30, 2, 'Thrombocyte', 7)

		self.image = pygame.image.load('res/thrombocyte.PNG')
		self.rect = self.image.get_rect()

	def Shoot(self, virus, bulletGroup):
		diff = time() - self.time
		if diff >= 1.00/self.shoot and virus.visible:
			if virus.name == 'ebola':
				bulletGroup.add(bullet(self.rect.center[0], self.rect.center[1], 1, 20, virus))
			else:
				bulletGroup.add(bullet(self.rect.center[0], self.rect.center[1], 1, 10, virus))
			self.time = time()
