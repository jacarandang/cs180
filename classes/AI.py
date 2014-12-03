from DS import *

class VirusNode(Node):

	def __init__(self, pos, board, parent = None):
		Node.__init__(self, pos, parent)
		self.board = board
		
	def nextNodes(self):
		dx = [-1, 0, 0, 1]
		dy = [0, -1, 1, 0]
		
		nxt = []
		for i in xrange(4):
			nx = self.state[0] + dx[i]
			ny = self.state[1] + dy[i]
			if nx >= 0 and nx < self.board.w and ny >= 0 and ny < self.board.h:
				if self.board.get(nx, ny) == 0:
					nxt.append(VirusNode((nx, ny), self.board, self))
		
		return nxt
	def isTarget(self):
		if self.state[0] == self.board.w-1:
			return True
		return False
		
	def __repr__(self):
		return str(self.state)
		
def DFS(node):
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
	if done:
		cur = n
		while(True):
			path.insert(0, cur.state)
			if cur.parent is None:
				break
			cur = cur.parent
	
	return path
