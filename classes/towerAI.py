import pygame
from pygame.locals import *
from tower import *
import pickle

class Action:

	def __init__(self, action, tower = None, pos = None, tower_d = None, tower_d_pos = []):
		self.action = action
		self.tower = tower
		self.pos = pos
		self.tower_d = tower_d
		self.tower_d_pos = tower_d_pos
		
class TowerPlayer:

	def __init__(self, res, tlist, tgroup, grid, game):
		self.towers = []
		self.actions = []
		with file('actions', 'rb') as f:
			self.actions = pickle.load(f)
		
		self.res = res
		self.tlist = tlist
		self.tgroup = tgroup
		self.grid = grid
		self.game = game
		self.tnames = ["Stem Cell", "Lymphocyte", "Natural Killer Cell", "T-Cell", "B-Cell", "Plasma Cell", "Granulocyte", "Basophil", "Neutrophil", "Eosinophil", "Monocyte", "Macrophage", "Megakaryocyte", "Thrombocyte"]
		self.tclasses = [StemCell, Lymphocyte, NaturalKillerCell, TCell, BCell, PlasmaCell, Granulocyte, Basophil, Neutrophil, Eosinophil, Monocyte, Macrophage, Megakaryocyte, Thrombocyte]
		
	def getTower(self, tower):
		for i in xrange(len(self.tnames)):
			if self.tnames[i] == tower:
				return self.tclasses[i]()
		
	def searchTower(self, pos):
		for t in self.tlist:
			if t.occupy == pos:
				return t 	
				
	def getActions(self):
		done = []
		if len(self.actions) == 0 and self.game.status == "prep": self.game.waveg()
		hasdone = False
		for action in self.actions:
			if action.action == 'buy':
				t = self.getTower(action.tower)
				print action.tower, t
				if self.res.currentATP - t.cost <= 0: break
				for i in action.pos:
					self.grid.set(i[0],i[1],1)
				t.setOccupy(action.pos)
				self.tgroup.add(t)
				self.tlist.append(t)
				self.res.currentATP -= t.cost
				done.append(action)
				hasdone = True
			elif action.action == 'sell':
				t = self.searchTower(action.tower_d_pos)
				t.kill()
				self.res.currentATP += t.cost
				done.append(action)
				hasdone = True
			elif action.action == 'upgrade':
				t = self.getTower(action.tower)
				if self.res.currentATP - t.cost <= 0: break
				t_d = self.searchTower(action.tower_d_pos)
				t_d.kill()
				
				for i in self.tlist:
					present = False
					for j in self.tgroup:
						if j == i:
							present = True
					if present == False:
						for k in i.occupy:
							self.grid.set(k[0],k[1],0)
						self.tlist.remove(i)
				
				for i in action.pos:
					self.grid.set(i[0],i[1],1)
					
				t.setOccupy(action.pos)
				self.tgroup.add(t)
				self.tlist.append(t)
				self.res.currentATP -= t.cost
				done.append(action)
				hasdone = True
			break
			
		if not hasdone and self.game.status == "prep":
			print "game"
			self.game.waveg()
		
		for a in done:
			self.actions.remove(a)

			
class Recorder:

	def __init__(self):
		self.actions = []
		
	def addAction(self, action):
		self.actions.append(action)
		
	def save(self):
		with file('actions', 'wb') as f:
			pickle.dump(self.actions, f)