from move import Move
from copy import deepcopy

class King():
	def __init__(self, side):
		self.side = side
		if self.side == 'w':
			self.pos = (0, 4)
		elif self.side == 'b':
			self.pos = (7, 4)
		self.check = False

	def move(self, pos):
		board[self.pos[0]][self.pos[1]] = None
		self.pos = pos
		board[pos[0]][pos[1]] = self 

	def get_actions(self, board):
		# Make this after the other classes are done
		actions = []
		x, y = self.pos
		dummy = deepcopy(board)
		enemy_actions = dummy.get_all_actions(side = 'b' if self.side == 'w' else 'w')

		# Check 5x5 square for enemy King
		enemy_king = get_king(side = 'b' if self.side == 'w' else 'w')

		# Square South
		if enemy_king.pos not in [(x+2, y), (x+2, y-1), (x+2, y+1)]:
			if x+1 < 8 and (x+1, y) not in enemy_actions:
				actions.append(Move(self, self.pos, (x+1, y)))

		# Square South West
		if enemy_king.pos not in [(x, y-2), (x+1, y-2), (x+2, y-2), (x+2, y-1), (x+2, y)]:
			if x+1 < 8 and y-1 >= 0 and (x+1, y-1) not in enemy_actions:
				actions.append(Move(self, self.pos, (x+1, y-1)))
		# Square West		
		if x+1 < 8 and (x+1, y) not in enemy_actions:
			actions.append(Move(self, self.pos, (x+1, y)))
		if x-1 >=0 and (x-1, y) not in enemy_actions:
			actions.append(Move(self, self.pos, (x-1, y)))
		if y+1 < 8 and (x, y+1) not in enemy_actions:
			actions.append(Move(self, self.pos, (x, y+1)))
		if y-1 >= 0 and (x, y-1) not in enemy_actions:
			actions.append(Move(self, self.pos, (x, y-1)))
		if x+1 < 8 and y+1 < 8 and (x+1, y+1) not in enemy_actions:
			actions.append(Move(self, self.pos, (x+1, y+1)))
		if x+1 < 8 and y-1 >= 0 and (x+1, y-1) not in enemy_actions:
			actions.append(Move(self, self.pos, (x+1, y-1)))
		if x-1 >= 0 and y+1 < 8 and (x-1, y+1) not in enemy_actions:
			actions.append(Move(self, self.pos, (x-1, y+1)))
		if x-1 >= 0 and y-1 >= 0 and (x-1, y-1) not in enemy_actions:
			actions.append(Move(self, self.pos, (x-1, y-1)))
		return actions

	def __str__(self):
		return 'k'

class Queen():
	def	__init__(self, side, pos):
		self.side = side
		self.pos = pos

	def move(self, pos, board):
		board[self.pos[0]][self.pos[1]] = None
		self.pos = pos
		board[pos[0]][pos[1]] = self 

	def get_actions(self, board):
		# Get the board

		# Get the queens postion
		x, y = self.pos

		#Initialize the actions array
		actions = []

		# Get all  actions where queen can go vertical and horizontal

		actions = []
		vert = get_vertical(self, board)
		horz = get_horizontal(self, board)
		if vert != None:
			actions.extend(vert)
		if horz != None:
			actions.extend(horz)

		# Diagonals
		diagonals = get_diagonal(self, board)
		if diagonals != None:
			actions.extend(diagonals)


		return actions
			
	def __str__(self):
		return 'q'

class Knight():
	def __init__(self, side, pos):
		self.side = side
		self.pos = pos

	def move(self, pos, board):
		board[self.pos[0]][self.pos[1]] = None
		self.pos = pos
		board[pos[0]][pos[1]] = self 

	def get_actions(self, board):
		actions = []
		x, y = self.pos
		offsets = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, -2), (1, 2), (2, 1), (2, -1)]
		for offset in offsets:
			if not x + offset[0] in [i for i in range(8)] or not y + offset[1] in [i for i in range(8)]:
				continue
			square = board[x+offset[0]][y+offset[1]]
			if square != None:
				if square.side != self.side:
					actions.append(Move(self, self.pos, (x+offset[0], y+offset[1])))
			else:
				actions.append(Move(self, self.pos, (x+offset[0], y+offset[1])))
		return actions


	def __str__(self):
		return 'n'

class Bishop():
	def __init__(self, side, pos):
		self.side = side
		self.pos = pos

	def move(self, pos, board):
		board[self.pos[0]][self.pos[1]] = None
		self.pos = pos
		board[pos[0]][pos[1]] = self 

	def get_actions(self, board):
		actions = get_horizontal(self, board)
		if actions == None:
			return []
		else:
			return actions
		
	def __str__(self):
		return 'b'

class Rook():
	def __init__(self, side, pos):
		self.side = side
		self.pos = pos
	
	def move(self, pos, board):
		board[self.pos[0]][self.pos[1]] = None
		self.pos = pos
		board[pos[0]][pos[1]] = self

	def get_actions(self, board):
		actions = []
		vert = get_vertical(self, board)
		horz = get_horizontal(self, board)
		if vert != None:
			actions.extend(vert)
		if horz != None:
			actions.extend(horz)
		return actions
		
	def __str__(self):
		return 'r'
		
class Pawn():
	def __init__(self, side, pos):
		self.side = side
		self.pos = pos
		self.first_move = False

	def move(self, move, board):
		if abs(self.pos[0] - move.end_pos[0]) == 2:
			self.first_move = True
		else:
			self.first_move = False
		board[self.pos[0]][self.pos[1]] = None
		self.pos = move.end_pos

		match move.promoted_peice:
			case 'q':
				board[move.end_pos[0]][move.end_pos[1]] = Queen(side = self.side, pos = move.end_pos)
			case 'r':
				board[move.end_pos[0]][move.end_pos[1]] = Rook(side = self.side, pos = move.end_pos)
			case 'b':
				board[move.end_pos[0]][move.end_pos[1]] = Bishop(side = self.side, pos = move.end_pos)
			case 'n':
				board[move.end_pos[0]][move.end_pos[1]] = Knight(side = self.side, pos = move.end_pos)
			case _:
				board[pos[0]][pos[1]] = self 
			

	def get_actions(self, board, enpassant = False):
		actions = []
		x, y = self.pos

		# Multiplier for both sides
		mpl = 1 if self.side == 'w' else -1

		# Normal case
		if  0 <= x+(1*mpl) < 8:
			if board[x+(1*mpl)][y] == None:
				# Check if pawn is promoting
				if (x == 6 and self.side == 'w') or (x == 1 and self.side == 'b'):
					actions.append(Move(self, self.pos, (x+(1*mpl)), y, 'q'))
					actions.append(Move(self, self.pos, (x+(1*mpl), y, 'n')))
					actions.append(Move(self, self.pos, (x+(1*mpl), y, 'b')))
					actions.append(Move(self, self.pos, (x+(1*mpl), y, 'r')))
				else:
					actions.append(Move(self, self.pos, (x+(1*mpl), y)))


		# First move 
		if (self.side == 'w' and x == 1) or (self.side == 'b' and x == 6):
			if board[x+(2*mpl)][y] == None and board[x+(1*mpl)][y] == None:
				actions.append(Move(self, self.pos, (x+(2*mpl), y)))

		# Captures
		for i in range(2):
			n = 1 if i == 0 else -1
			if 0 <= x+(1*mpl) < 8 and 0 <= y+n < 8:
				if board[x+(1*mpl)][y+n] != None:
					if board[x+(1*mpl)][y+n].side != self.side:
						if (x == 6 and self.side == 'w') or (x == 1 and self.side == 'b'):
							actions.append(Move(self, self.pos, (x+(1*mpl), y+n), 'q'))
							actions.append(Move(self, self.pos, (x+(1*mpl), y+n), 'n'))
							actions.append(Move(self, self.pos, (x+(1*mpl), y+n), 'b'))
							actions.append(Move(self, self.pos, (x+(1*mpl), y+n), 'r'))
						else:
							actions.append(Move(self, self.pos, (x+(1*mpl), y)))

		# En passant captures
		for i in range(2):
			n = 1 if i == 0 else -1
			if 0 <= x+(1*mpl) < 8 and 0 <= y+n < 8:
				if board[x+(1*mpl)][y+n] == None and type(board[x][y+n]) == type(Pawn('w', (0,0))):
					if board[x][y+n].side != self.side and board[x][y+n].first_move == True:
						actions.append((x+(1*mpl), y+n))
		return actions

	def __str__(self):
		return 'p'

def get_king(side, board):
	for row in board.board:
		for sq in row:
			if type(sq) == type(King(side = 'w')):
				if sq.side == side:
					return sq

def get_vertical(peice, board):
	x, y = peice.pos
	actions = []
	for i in range(x+1, 8):
		if board[i][y] != None:
			if board[i][y].side != peice.side:
				actions.append(Move(peice, peice.pos, (i, y)))
			break
		actions.append((i, y))
	
	for i in [num for num in range(x)][::-1]:
		if board[i][y] != None:
			if board[i][y].side != peice.side:
				actions.append(Move(peice, peice.pos, (i, y)))
			break
		actions.append((i, y))

	return actions

def get_horizontal(peice, board):
	x, y = peice.pos
	actions = []
	for i in range(y+1, 8):
		if board[x][i] != None:
			if board[x][i].side != peice.side:
				actions.append(Move(peice, peice.pos, (x, i)))
			break
		actions.append((x, i))
	for i in [j for j in range(y)][::-1]:
		if board[x][i] != None:
			if board[x][i].side != peice.side:
				actions.append(Move(peice, peice.pos, (x, i)))
			break
		actions.append((x, i))
	return actions

def get_diagonal(peice, board):
	actions = []
	x, y = peice.pos
	i = 1
	while True:
		if x+i > 7 or y+i > 7:
			break
		if board[x+i][y+i] != None:
			if board[x+i][y+i].side != peice.side:
				actions.append(Move(peice, peice.pos, (x+i, y+i)))
			break
		actions.append(Move(peice, peice.pos, (x+i, y+i)))

		i+=1
	i= 1
	while True:
		if x-i < 0 or y-i < 0:
			break
		if board[x-i][y-i] != None:
			if board[x-i][y-i].side != peice.side:
				actions.append(Move(peice, peice.pos, (x-i, y-i)))
			break
		actions.append(Move(peice, peice.pos, (x-i, y-i)))

		i+=1
	i=1
	while True:
		if x-i < 0 or y+i < 0:
			break
		if board[x-i][y+i] != None:
			if board[x-i][y+i].side != peice.side:
				actions.append(Move(peice, peice.pos, (x-i, y+i)))
			break
		actions.append(Move(peice, peice.pos, (x-i, y+i)))

		i+=1
	i=1
	while True:
		if x+i < 8 or y-i >= 0:
			break
		if board[x+i][y-i] != None:
			if board[x+i][y-i].side != peice.side:
				actions.append(Move(peice, peice.pos, (x+i, y-i)))
			break
		actions.append(Move(peice, peice.pos, (x+i, y-i)))

		i+=1
	return actions