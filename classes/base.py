class Board

	def __init__(self, w, h):
		self.w = w
		self.h = h
		self.board = []
		for i in xrange(w):
			arr = []
			for self j in xrange(h):
				arr.append(0)
			self.board.append(arr)
	
	def get(r, c):
		return self.board[r][c]
	
	def set(r, c, val):
		self.board[r][c] = val
		