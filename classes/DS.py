class Stack:

	def __init__(self):
		self.list = []
		
	def push(self, obj):
		self.list.append(obj)
		
	def pop(self, idx = 0):
		return self.list.pop(idx)
		
	def isEmpty(self):
		if len(self.list) == 0:
			return True
		return False
		
class Node:

	def __init__(self, state, parent = None):
		self.state = state
		self.parent = parent
		
	def nextNodes(self):
		return []
		
	def isTarget(self):
		return False
		
	def __eq__(self, other):
		return self.state == other.state