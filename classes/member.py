import pygame
from pygame.locals import *
from random import uniform, random
class Member:

	def __init__(self, values = None, wave = None):
		self.value = values
		if self.value is None: self.value = [uniform(-1, 1) for i  in xrange(14*6)]
		self.wave = wave
		if self.wave is None: self.wave = [uniform(-1, 1) for i in xrange(6)]
		self.fitness = 0
	
	def mutate(self):
		for i in xrange(len(self.value)):
			if random() > 0.5:
				self.value[i] += uniform(-.1, .1)
		for i in xrange(len(self.wave)):
			if random() > 0.5:
				self.wave[i] += uniform(-.1, .1)
				
	def crossover(self, other):
		vals = []
		nwave = []
		a_val = self.value
		b_val = other.value
		for i in xrange(len(a_val)):
			if random() > 0.5:
				vals.append(a_val[i])
			else:
				vals.append(b_val[i])
		for i in xrange(len(self.wave)):
			if random() > 0.5: nwave.append(self.wave[i])
			else: nwave.append(other.wave[i])
		m = Member(vals, nwave)
		if random() <= 0.05:
			m.mutate()
		return m
		
	def __eq__(self, other):
		if other == None: return False
		return self.fitness == other.fitness
		
	def __cmp__(self, other):
		return self.fitness - other.fitness
		
	def __repr__(self):
		return str(self.fitness)