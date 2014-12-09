from random import uniform, random, randint, choice
import pickle
from main import Game
import pygame
import os
pygame.init()
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
				
	def evaluate(self):
		scr = pygame.display.set_mode((800,600))
		g = Game(scr)
		a = g.start()
		if g.thing.life < 0:
			g.thing.life = 0
		self.fitness = (g.thing.full - g.thing.life)/g.wave
		raw_input("Fitness of " + str(self.fitness) + ": (Press enter to continue)")
		return self.fitness
		
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
		
	def __cmp__(self, other):
		return self.fitness - other.fitness
		
	def __repr__(self):
		return str(self.fitness)

class Genetic:

	def __init__(self, population = None):
	
		self.pop = population
		if self.pop is None: self.pop = [Member() for i in xrange(10)]
				
	def mutation(self, member):
		member.mutate()
		
	def avg(self, pop):
		s = sum([p.fitness for p in pop])
		return s*1.00/len(pop)
		
	def start(self, generations = 10):
		pop = self.pop
		for i in xrange(generations):
			for m in pop:
				m.evaluate()
			breed = []			#parents for breeding
			while not len(pop) == 0:
				a = choice(pop)
				pop.remove(a)
				b = choice(pop)
				pop.remove(b)
				if a > b:
					breed.append(a)
				else:
					breed.append(b)
			n_pop = []			#new population
			for i in xrange(10):
				a = choice(breed)
				b = choice(breed)
				n_pop.append(a.crossover(b))
			pop = n_pop
			
		for m in pop:
			m.evaluate()
		return pop

dir = 'ai'
g = Genetic()
pop  = g.start(10)