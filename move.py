class Move():
	def __init__(self, peice, start_pos, end_pos, promoted_peice = None):
		self.peice = peice
		self.start_pos = start_pos
		self.end_pos = end_pos
		self.promoted_peice = promoted_peice