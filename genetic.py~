from random import uniform, random, randint, choice
import pickle
from main import Game
import pygame
import os
from classes.member import Member
pygame.init()

class Genetic:

	def __init__(self, space = 10, population = None):
	
		self.pop = population
		self.space = space
		if self.pop is None: self.pop = [Member() for i in xrange(space)]
				
	def evaluate(self, member):
		scr = pygame.display.set_mode((800,600))
		g = Game(scr, member)
		a = g.start()
		if g.thing.life < 0:
			g.thing.life = 0
		member.fitness = (g.thing.full - g.thing.life)/g.wave
		raw_input("Fitness of " + str(member.fitness) + ": (Press enter to continue)")
		return member.fitness			
	
	def mutation(self, member):
		member.mutate()
		
	def avg(self, pop):
		s = sum([p.fitness for p in pop])
		return s*1.00/len(pop)
		
	def start(self, generations = 10):
		pop = self.pop
		for i in xrange(generations):
			for m in pop:
				self.evaluate(m)
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
			for i in xrange(self.space):
				a = choice(breed)
				b = choice(breed)
				n_pop.append(a.crossover(b))
			pop = n_pop
			
		for m in pop:
			self.evaluate(m)
		return pop

dir = 'ai'
g = Genetic(2)
pop  = g.start(1)
pop.sort(reverse = True)
with file(os.path.join(dir, 'data.net'), "wb") as f:
	pickle.dump(pop, f)