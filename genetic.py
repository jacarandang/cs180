from random import uniform, random, randint, choice
import pickle
from main import Game
import pygame
pygame.init()
class Member:

	def __init__(self, values = None):
		self.value = values
		if self.value is None: self.value = [uniform(-.5, .5) for i  in xrange(14*6)]
		self.fitness = 0
	
	def mutate(self):
		for i in xrange(len(self.value)):
			if random() > 0.5:
				self.value[i] += uniform(-.1, .1)
				
	def evaluate(self):
		scr = pygame.display.set_mode((800,600))
		g = Game(scr)
		a = g.start()
		if g.thing.life < 0:
			g.thing.life = 0
		self.fitness = (g.thing.full - g.thing.life)/g.wave
		print self.fitness
		raw_input()
		return self.fitness
		
	def __cmp__(self, other):
		return self.fitness - other.fitness
		
	def __repr__(self):
		return str(self.fitness)

class Genetic:

	def __init__(self, population = None):
	
		self.pop = population
		if self.pop is None: self.pop = [Member() for i in xrange(10)]
		
	def crossover(self, a, b):
		a_pop = a.value
		b_pop = b.value
		n_pop = []
		for i in xrange(len(a_pop)):
			if randint(0, 1) == 0:
				n_pop.append(a_pop[i])
			else:
				n_pop.append(b_pop[i])
		m = Member(n_pop)
		if random() >= 0.05:
			m.mutate()
		return m
				
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
				n_pop.append(self.crossover(a, b))
			pop = n_pop
			
		for m in pop:
			m.evaluate()
		return pop

g = Genetic()
pop  = g.start(10)