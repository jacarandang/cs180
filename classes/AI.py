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
			if nx >= 0 and nx < 20 and ny >= 0 and ny < 16:
				if self.board.get(nx, ny) == 0:
					nxt.append(Node((nx, ny), board, self))
			
	def isTarget(self):
		if self.x == 15:
			return True
		return False
		
class AIfxn:

	def DFS(node):
		s = Stack()
		s.push(node)
		
		visited = []
		done = False
		n = None
		while(!s.isEmpty()):
			n = s.pop()
			if n.isTarget():
				done = True
				break
			nxt = n.nextNodes()
			
			if n in visited:
				continue
			for nodes in nxt:
				if nodes in visited: continue
				s.push(nodes)
				
		path = []
		if done:
			while(True):
				cur = n:
				path.insert(0, n)
				if cur.parent is None:
					break
				cur = n.parent
		
		return path
	