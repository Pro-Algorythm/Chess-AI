class Move():
	def __init__(self, peice, start_pos, end_pos, promoted_peice = None, castling = None):
		self.peice = peice
		self.start_pos = start_pos
		self.end_pos = end_pos
		self.promoted_peice = promoted_peice
		self.castling = castling
	def __str__(self):
		return f"{'White' if self.peice.side == 'w' else 'Black'} {str(self.peice).upper()} goes from {self.start_pos} to {self.end_pos}\n"