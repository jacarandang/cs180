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
