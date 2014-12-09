import pygame
from pygame.locals import *
from virus import *
from AI import *
from pickle import *
from random import shuffle
class Player():

	def __init__(self, board, thing, tower, values = None, atp = None):
		self.board = board
		self.thing = thing
		self.tower = tower
		self.values = values
		self.e = Evaluator(values)
		self.atp = atp
		self.vcosts = [1, 5, 10, 7, 10, 20]
		print self.atp.currentVirusATP
		
	def hasValidPath(self, board):
		p = []
		cost = 0
		for i in xrange(board.h):
			if board.get(0, i) == 0:
				n = VirusNode((0, i), board)
				p, cost = DFS(n)
				if p!=[]:
					print p[0]
					return True
					
		return False
		
	def force(self):
		#v = Fungi(self.board, self.thing)
		group = VirusGroup()
		for i in xrange(30):
			group.add(Fungi(self.board, self.thing))
		
		#for i in xrange(1):
		#	group.add(HIV(self.board, self.thing))

		#for i in xrange(50):
		#	group.add(Ebola(self.board, self.thing))

		p = []
		for i in xrange(self.board.h):
			if self.board.get(0, i) == 0:
				n = VirusNode((0, i), self.board)
				temp_p, temp_cost = BFS(n)
				if temp_p != []:
					p = temp_p
					break
					
		group.setActions(p)
		
		return group
		
	def getNextGroup(self):
		group = VirusGroup()
		group.add()

		p = []
		cost = 400
		for i in xrange(self.board.h):
			if self.board.get(0, i) == 0:
				n = VirusNode((0, i), self.board)
				temp_p, temp_cost = BFS(n)
				if temp_p != []:
					if temp_cost < cost:
						p = temp_p
						cost = temp_cost
				
		inrange = []
		for pos in p:
			for t in self.tower:
				if t in inrange: continue
				if t.inRange(pos): inrange.append(t)
		
		ntowers = [0 for i in xrange(14)]
		nnames = ["Stem Cell", "Lymphocyte", "Natural Killer Cell", "T-Cell", "B-Cell", "Plasma Cell", "Granulocyte", "Basophil", "Neutrophil", "Eosinophil", "Monocyte", "Macrophage", "Megakaryocyte", "Thrombocyte"]
		for t in inrange:
			for i in xrange(len(nnames)):
				if t.tower_type == nnames[i]:
					ntowers[i] += 1
					break
		
		prop = self.e.eval(ntowers, 6)
		prop_cost = 0
		for i in xrange(6):
			prop_cost += self.vcosts[i] * prop[i]
		num = int(self.atp.currentVirusATP/prop_cost)
		print num
		
		nhiv = int(num * prop[5])
		print nhiv
		for i in xrange(nhiv): group.add(HIV(self.board, self.thing, self.atp))
		self.atp.currentVirusATP -= nhiv * self.vcosts[5]
		
		nebo = int(num * prop[4])
		for i in xrange(nebo): group.add(Ebola(self.board, self.thing, self.atp))
		self.atp.currentVirusATP -= nebo * self.vcosts[4]
		
		nvir = int(num * prop[3])
		for i in xrange(nvir): group.add(Virus(self.board, self.thing, self.atp))
		self.atp.currentVirusATP -= nvir * self.vcosts[3]
		
		nbac = int(num * prop[2])
		for i in xrange(nbac): group.add(Bacteria(self.board, self.thing, self.atp))
		self.atp.currentVirusATP -= nbac * self.vcosts[2]
		
		npar = int(num * prop[1])
		for i in xrange(npar): group.add(Parasite(self.board, self.thing, self.atp))
		self.atp.currentVirusATP -= npar * self.vcosts[1]
		
		nfun = self.atp.currentVirusATP
		for i in xrange(nfun): group.add(Fungi(self.board, self.thing, self.atp))
		self.atp.currentVirusATP -= nfun * self.vcosts[0]
		
		group.setActions(p)
		shuffle(group.hvirus)
		return group
		
	def getPath(self): 
		board = self.board.board
		for i in xrange(self.board.w):
			for j in xrange(self.board.h):
				if board[i][j]:
					board[i][j] = -1
		
		one = [(-1, 1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		two = [(-1, -1)]
		for t in self.tower:
			d = t.damage * t.shoot
			r = t.radius/30.00
			mid = (t.occupy[-1][0] + t.occupy[0][0])/2, (t.occupy[-1][1] + t.occupy[0][1])/2
			print mid, r
			tl = int(mid[0] - r), int(mid[1] - r)
			br = int(mid[0] + r), int(mid[1] + r)
			print tl
			print tl[0]+ 2*r, tl[1] + 2*r
