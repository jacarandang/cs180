from DS import *
from random import uniform

class VirusNode(Node):

	def __init__(self, pos, board, parent = None, cost = 0):
		Node.__init__(self, pos, parent)
		self.board = board
		self.cost = cost
		
	def nextNodes(self):
		dx = [-1, 0, 0, 1]
		dy = [0, -1, 1, 0]
		
		nxt = []
		for i in xrange(4):
			nx = self.state[0] + dx[i]
			ny = self.state[1] + dy[i]
			if nx >= 0 and nx < self.board.w and ny >= 0 and ny < self.board.h:
				if self.board.get(nx, ny) == 0:
					nxt.append(VirusNode((nx, ny), self.board, self, self.cost + 1))
		
		return nxt
	def isTarget(self):
		if self.state[0] == self.board.w-1:
			return True
		return False
		
	def __repr__(self):
		return str(self.state)
		
	def __cmp__(self, other):
		return other.cost - self.cost
		
def BFS(node):
	s = Queue()
	s.push(node)
	
	visited = []
	done = False
	n = None
	while not s.isEmpty():
		n = s.pop()
		
		if n in visited:
			continue
		visited.append(n)
			
		if n.isTarget():
			done = True
			break
			
		nxt = n.nextNodes()
		
			
		for nodes in nxt:
			if nodes in visited:
				continue
			s.push(nodes)
			
	path = []
	cost = 0
	if done:
		cost = n.cost
		cur = n
		while(True):
			path.insert(0, cur.state)
			if cur.parent is None:
				break
			cur = cur.parent
	
	return path, cost

def DFS(node):
	s = Stack()
	s.push(node)
	
	visited = []
	done = False
	n = None
	while not s.isEmpty():
		n = s.pop()
		
		if n in visited:
			continue
		visited.append(n)
			
		if n.isTarget():
			done = True
			break
			
		nxt = n.nextNodes()
		
			
		for nodes in nxt:
			if nodes in visited:
				continue
			s.push(nodes)
			
	path = []
	cost = 0
	if done:
		cost = n.cost
		cur = n
		while(True):
			path.insert(0, cur.state)
			if cur.parent is None:
				break
			cur = cur.parent
	
	return path, cost
	
def UCS(node):
	pq = PQ()
	pq.push(node)
	visited = []
	done = False
	n = None
	while not pq.isEmpty():
		n = s.pop()
		
		if n in visited:
			continue
		visited.append(n)
		
		if n.isTarget():
			done = True
			break
		
		nxt = n.nextNodes()
		
		for nodes in nxt:
			if nodes in visited:
				continue
			s.push(nodes)
			
		path = []
		
	if done:
		cur = n
		while(True):
			path.insert(0, cur.state)
			if cur.parent is None:
				break
			cur = cur.parent
	
	return path

class Evaluator:

	def __init__(self, values = None):
		self.values = values
		if self.values == None: self.values = [uniform(-0.5, 0.5) for i in xrange(14 * 6)]
		
	def eval(self, ntowers, nvirus):
		total = [0 for i in xrange(nvirus)]
		for i in xrange(nvirus):
			for j in xrange(len(ntowers)):
				total[i] += ntowers[j]*self.values[i*14 + j]
		
		mn = min(total)
		if mn < 0:
			for i in xrange(len(total)): total[i] += mn
		
		s = sum(total)
		if s == 0:
			for i in xrange(len(total)):
				total[i] += uniform(0, 0.25)
			mn = min(total)
			if mn < 0:
				for i in xrange(len(total)): total[i] += mn
			s = sum(total)
		for i in xrange(len(total)):
			total[i] /= s
			
		return total
		