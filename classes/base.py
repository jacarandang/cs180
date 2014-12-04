import pygame

class Board:

	def __init__(self, w=20, h=16, coor=(0,0)):
		self.w = w
		self.h = h
		self.coor = coor
		self.board = []
		for i in xrange(self.w):
			arr = []
			for j in xrange(self.h):
				arr.append(0)
			self.board.append(arr)
	
	def get(self, r, c):
		return self.board[r][c]
	
	def set(self, r, c, val):
		self.board[r][c] = val

	def coorToIndex(self, m_pos, size):
		return ((self.coor[0]+m_pos[0])/size, (self.coor[1]+m_pos[1])/size)

	def draw(self, size=30, screen=None):
		y = self.coor[1]
		for i in range(self.h):
			x = self.coor[0]
			for j in range(self.w):
				if self.board[j][i] == 1:
					pygame.draw.rect(screen,(255,0,0),(x, y, size, size), 1)
				else:
					pygame.draw.rect(screen,(0,0,0),(x, y, size, size), 1)
				x += size
			y += size

	def detect(self, m_pos, tower, screen):
		listContains = []

		m_ypos = m_pos[1]
		for a in range(tower.h):
			m_xpos = m_pos[0]
			for b in range(tower.w):
				if self.getIndexDetect != False:
					listContains.append(self.getIndexDetect((m_xpos,m_ypos), tower, screen))
				else:
					return False
				m_xpos += tower.size
			m_ypos += tower.size

		return listContains


	def getIndexDetect(self, m_pos, tower, screen):
		x = self.coorToIndex(m_pos, tower.size)[0]
		y = self.coorToIndex(m_pos, tower.size)[1]
		
		if x < 0 or y < 0 or x >= self.w or y >= self.h:
			return False

		y_1 = self.coor[1]
		for i in range(self.h):
			x_1 = self.coor[0]
			for j in range(self.w):
				if i == y and j == x:
					if self.board[j][i] == 0:
						pygame.draw.rect(screen, (255,255,51),(x_1, y_1, tower.size, tower.size), 0)	
					else:
						pygame.draw.rect(screen, (255,0,0),(x_1, y_1, tower.size, tower.size), 0)	
				x_1 += tower.size				
			y_1 += tower.size

		return (x,y)
	
class VirusBase:
	
	def __init__(self, board, life=10, speed=1):
		self.life = life
		self.speed = speed
		self.board = board
		self.step = 0
		self.x = 0
		self.y = 0
		self.group = None
		self.dmg = 1
		self.rod = .5	#rate of damage
		
	def getCurrentAction(self):
		if self.group is None: 
			return None
		return self.group.getAction(self.step)
	
	def getNextAction(self):
		if self.group is None: return None
		return self.group.getAction(self.step + 1)
	
	def setNextAction(self):
		self.step += 1
		
	def damage(self, dmg):
		self.life -= dmg
		
	def __repr__(self):
		return 'virus'
		
class VirusGroupBase:
	
	def __init__(self, *vrs):
		self.viruses = []
		self.add(*vrs)
		self.actionList = []
		for v in self.viruses:
			v.group = self
			
	def add(self, *vrs):
		for virus in vrs:
			self.viruses.append(virus)
			virus.group = self
		
	def setActions(self, actions):
		self.actionList = actions
		
	def getAction(self, idx):
		if(idx >= len(self.actionList)): return None
		return self.actionList[idx]

class Thing:

	def __init__(self, life = 1000):
		self.full = life
		self.life = life
		
	def damage(self, damage):
		self.life -= damage
		
	def  isDead(self):
		if self.life <= 0:
			return True
		return False
		
	def percentage(self):
		return self.life/self.full*1.00
