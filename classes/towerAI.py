import pygame
from pygame.locals import *
from tower import *

class Action:

	def __init__(self, action, tower, pos, tower_d = None):
		self.action = action
		self.tower = tower
		self.pos = pos
		self.tower_d = tower_d
		
class TowerPlayer:

	def __init__(self, res, tlist, tgroup, grid, game):
		a = StemCell()
		self.actions = [
			Action('buy', a, [(0, 0)]),
			Action('upgrade', Lymphocyte(), [(0, 0)], a)
		]
		self.res = res
		self.tlist = tlist
		self.tgroup = tgroup
		self.grid = grid
		self.game = game
		
	def getActions(self):
		done = []
		for action in self.actions:
			if action.action == 'buy':
				t = action.tower
				if self.res.currentATP - t.cost <= 0: break
				t.setOccupy(action.pos)
				self.tgroup.add(t)
				self.tlist.append(t)
				self.res.currentATP -= t.cost
			else:
				t = action.tower
				if self.res.currentATP - t.cost <= 0: break
				t.setOccupy(action.pos)
				self.tgroup.add(t)
				self.tlist.append(t)
				t_d = action.tower_d
				self.tlist.remove(t_d)
				t_d.kill()
				self.res.currentATP -= t.cost
			done.append(action)
		
		for a in done:
			self.actions.remove(a)
				