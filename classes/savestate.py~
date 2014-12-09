import pickle

class SaveState():
	def __init__(self):
		self.grid = None
		self.tower_list = []
		self.wave = 0
		self.atp = 0
		self.virus_atp = 0

	def save(self, grid, tower_list, wave, atp, virus_atp):
		self.grid = grid
		for i in tower_list:
			self.tower_list.append(i)
		self.wave = wave
		self.atp = atp
		self.virus_atp = virus_atp

