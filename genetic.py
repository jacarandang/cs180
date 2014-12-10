from random import uniform, random, randint, choice
import pickle
from main import Game
import pygame
import os, sys, getopt
from classes.member import Member
pygame.init()

class Genetic:

	def __init__(self, space = 10, population = None, action = None):
	
		self.pop = population
		self.space = space
		if self.pop is None:
			self.pop = [Member() for i in xrange(space)]
		self.action = action
		if self.action == None:
			self.action = ['actions']
				
	def evaluate(self, member):
		scr = pygame.display.set_mode((800,600))
		ac = choice(self.action)
		g = Game(scr, member, None, ac)
		a = g.start()
		if g.thing.life < 0:
			g.thing.life = 0
		member.fitness = (g.thing.full - g.thing.life)/g.wave
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

if __name__ == '__main__':
	
	argv = sys.argv[1:]
	pop = 5
	gen = 10
	action = None
	populations = None
	outputF = 'data.net'
	try:
		opts, args = getopt.getopt(argv,"hp:g:a:n:o:")
	except getopt.GetoptError:
		print 'genetic.py	-p [# of population] -g [# of generation] -a [action files] -n [population files] -o [output]'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'genetic.py	-p [# of population] -g [# of generation] -a [action files] -n [population files] -o [output]'
			sys.exit()
		if opt == '-p':
			pop = int(arg)
		elif opt == '-g':
			gen = int(arg)
		elif opt == '-a':
			action = arg.split(',')
		elif opt == '-n':
			populations = arg.split(',')
		elif opt == '-o':
			outputF = arg
	
	
	members = []
	if populations is not None:
		for p in populations:
			with file(p, "rb") as f:
				n = pickle.load(f)
				for m in n:
					members.append(m)
	else:
		members = None
		
	g = Genetic(pop, members, action)
	pop  = g.start(gen)
	pop.sort(reverse = True)
	print "Last population with fitness"
	print pop
	with file(os.path.join(dir, outputF), "wb") as f:
		pickle.dump(pop, f)
