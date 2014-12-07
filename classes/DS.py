class Queue:

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
		
class Stack:

	def __init__(self):
		self.list = []
		
	def push(self, obj):
		self.list.append(obj)
		
	def pop(self, idx = -1):
		return self.list.pop(idx)
		
	def isEmpty(self):
		if len(self.list) == 0:
			return True
		return False
		
class PQ:

	def __init__(self):
		self.list = []
		
	def push(self, obj):
		self.list.append(obj)
		self.list.sort()
		
	def pop(self, idx):
		return self.list.pop(idx)
		
	def isEmpty(self):
		if len(self.list) == 0:
			return True
		return False
		
	def resort(self):
		self.list.sort()
		
class Node:

	def __init__(self, state, parent = None):
		self.state = state
		self.parent = parent
		
	def nextNodes(self):
		raise NotImplementedError
		
	def isTarget(self):
		raise NotImplementedError
		
	def __eq__(self, other):
		return self.state == other.state
		
	def __cmp__(self, other):
		raise NotImplementedError