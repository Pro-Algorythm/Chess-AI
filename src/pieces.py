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
		self.moved = False

	def move(self, move, board):
		state = board.board
		if move.castling != None:
			rook = state[0 if move.peice.side == 'w' else 7][7 if move.castling == 'kingside' else 0]
			rook.move(Move(rook, rook.pos, (0 if move.peice.side == 'w' else 7, 5 if move.castling == 'kingside' else 3)), board)
		state[self.pos[0]][self.pos[1]] = None
		self.pos = move.end_pos
		state[move.end_pos[0]][move.end_pos[1]] = self 
		self.moved = True

	def get_actions(self, board):
		# Initialize the actions array and get the position of the king
		actions = []
		x, y = self.pos

		# Check 5x5 square for enemy King
		enemy_king = get_king(side = 'b' if self.side == 'w' else 'w', board = board.board)

		# South
		if enemy_king.pos not in [(x+2, y), (x+2, y-1), (x+2, y+1)]:
			if x+1 < 8 and (board.board[x+1][y] == None or board.board[x+1][y].side == ('w' if self.side == 'b' else 'b')):
				dummy = deepcopy(board)
				king = dummy.board[self.pos[0]][self.pos[1]]
				move = Move(king, king.pos, (x+1, y))
				king.move(move, dummy)
				if king.pos not in [action.end_pos for action in dummy.get_all_actions(side = 'w' if self.side == 'b' else 'b')]:
					actions.append(Move(self, self.pos, (x+1, y)))
		# South West
		if enemy_king.pos not in [(x, y-2), (x+1, y-2), (x+2, y-2), (x+2, y-1), (x+2, y)]:
			if x+1 < 8 and y-1 >= 0 and (board.board[x+1][y-1] == None or board.board[x+1][y-1].side == ('w' if self.side == 'b' else 'b')):
				dummy = deepcopy(board)
				king = dummy.board[self.pos[0]][self.pos[1]]
				move = Move(king, king.pos, (x+1, y-1))
				king.move(move, dummy)
				if king.pos not in [action.end_pos for action in dummy.get_all_actions(side = 'w' if self.side == 'b' else 'b')]:
					actions.append(Move(self, self.pos, (x+1, y-1)))
		# East
		if enemy_king.pos not in [(x-1, y-2), (x, y-2), (x+1, y-2)]:
			if y+1 < 8 and (board.board[x][y+1] == None or board.board[x][y+1].side == ('w' if self.side == 'b' else 'b')):
				dummy = deepcopy(board)
				king = dummy.board[self.pos[0]][self.pos[1]]
				move = Move(king, king.pos, (x, y+1))
				king.move(move, dummy)
				if king.pos not in [action.end_pos for action in dummy.get_all_actions(side = 'w' if self.side == 'b' else 'b')]:
					actions.append(Move(self, self.pos, (x, y+1)))
		# North West
		if enemy_king.pos not in [(x-2, y), (x-2, y-1), (x-2, y-2), (x-1, y-2), (x, y-2)]:
			if x-1 >=  0 and y-1 >= 0 and (board.board[x-1][y-1] == None or board.board[x-1][y-1].side == ('w' if self.side == 'b' else 'b')):
				dummy = deepcopy(board)
				king = dummy.board[self.pos[0]][self.pos[1]]
				move = Move(king, king.pos, (x-1, y-1))
				king.move(move, dummy)
				if king.pos not in [action.end_pos for action in dummy.get_all_actions(side = 'w' if self.side == 'b' else 'b')]:
					actions.append(Move(self, self.pos, (x-1, y-1)))
		# North
		if enemy_king.pos not in [(x-2, y-1), (x-2, y), (x-2, y+1)]:
			if x-1 >= 0 and (board.board[x-1][y] == None or board.board[x-1][y].side == ('w' if self.side == 'b' else 'b')):
				dummy = deepcopy(board)
				king = dummy.board[self.pos[0]][self.pos[1]]
				move = Move(king, king.pos, (x-1, y))
				king.move(move, dummy)
				if king.pos not in [action.end_pos for action in dummy.get_all_actions(side = 'w' if self.side == 'b' else 'b')]:
					actions.append(Move(self, self.pos, (x-1, y)))
		# North East
		if enemy_king.pos not in [(x-2, y), (x-2,y+1), (x-2, y-2), (x-1, y+2), (x, y+2)]:
			if x-1 >= 0 and y+1 < 8 and (board.board[x-1][y+1] == None or board.board[x-1][y+1].side == ('w' if self.side == 'b' else 'b')):
				dummy = deepcopy(board)
				king = dummy.board[self.pos[0]][self.pos[1]]
				move = Move(king, king.pos, (x-1, y+1))
				king.move(move, dummy)
				if king.pos not in [action.end_pos for action in dummy.get_all_actions(side = 'w' if self.side == 'b' else 'b')]:
					actions.append(Move(self, self.pos, (x-1, y+1)))
		
					
		# South East
		if enemy_king.pos not in [(x, y+2), (x+1, y+2), (x+2, y+2), (x+2, y), (x+2, y+1)]:
			if x+1 < 8 and y+1 < 8 and (board.board[x+1][y+1] == None or board.board[x+1][y+1].side == ('w' if self.side == 'b' else 'b')):
				dummy = deepcopy(board)
				king = dummy.board[self.pos[0]][self.pos[1]]
				move = Move(king, king.pos, (x+1, y+1))
				king.move(move, dummy)
				if king.pos not in [action.end_pos for action in dummy.get_all_actions(side = 'w' if self.side == 'b' else 'b')]:
					actions.append(Move(self, self.pos, (x+1, y+1)))

		enemy_actions = [move.end_pos for move in board.get_all_actions(side = 'w' if self.side == 'b' else 'b')]
		if self.side == 'w':
			# Castling kingside
			if not self.moved and isinstance(board.board[0][7], Rook) and not self.check:
				if not board.board[0][7].moved:
					if all(square == None for square in [board.board[x][y+1], board.board[x][y+2]]) and (x, y+1) not in enemy_actions and (x, y+2) not in enemy_actions:
						actions.append(Move(self, self.pos, (x, y+2), castling = 'kingside'))
			# Castling queen side
			if not self.moved and isinstance(board.board[0][0], Rook) and not self.check:
				if not board.board[0][0].moved:
					if all(square == None for square in [board.board[x][y-1], board.board[x][y-2], board.board[x][y-3]]) and (x, y-1) not in enemy_actions and (x, y-2) not in enemy_actions and (x, y-3) not in enemy_actions:
						actions.append(Move(self, self.pos, (x, y-2), castling = 'queenside'))
		else:
			# Castling kingside
			if not self.moved and isinstance(board.board[7][0], Rook) and not self.check:
				if not board.board[7][0].moved:
					if all(square == None for square in [board.board[x][y+1], board.board[x][y+2]]) and (x, y-1) not in enemy_actions and (x, y-2) not in enemy_actions:
						actions.append(Move(self, self.pos, (x, y+2), castling = 'kingside'))
			# Castling queen side
			if not self.moved and isinstance(board.board[7][7], Rook) and not self.check:
				if not board.board[7][7].moved:
					if all(square == None for square in [board.board[x][y-1], board.board[x][y-2], board.board[x][y-3]]) and (x, y-1) not in enemy_actions and (x, y-2) not in enemy_actions and (x, y-3) not in enemy_actions:
						actions.append(Move(self, self.pos, (x, y-2), castling = 'queenside'))
		return actions

	def __str__(self):
		return 'k'

class Queen():
	def	__init__(self, side, pos):
		self.side = side
		self.pos = pos

	def move(self, move, board):
		state = board.board
		pos = move.end_pos
		state[self.pos[0]][self.pos[1]] = None
		self.pos = pos
		state[pos[0]][pos[1]] = self 

		# Get the enemy kings position and see if hes in check
		king = get_king(side = 'w' if self.side == 'b' else 'b', board = state)
		actions = self.get_actions(board)
		if king.pos in [move.end_pos for move in actions]:
			king.check=True
		else:
			king.check = False
		
	def get_actions(self, board, checking_pins = False):
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

		if not checking_pins:
			valid_moves = []
			for action in actions:
				# Create a deepcopy and get the queen
				dummy = deepcopy(board)
				queen = dummy.board[self.pos[0]][self.pos[1]]

				# Make the move
				move = Move(queen, queen.pos, action.end_pos)
				pos = move.end_pos
				dummy.board[self.pos[0]][self.pos[1]] = None
				queen.pos = pos
				dummy.board[pos[0]][pos[1]] = queen

				# Check if king is in check 
				king = get_king(side = self.side, board = dummy.board)
				enemy_actions = []
				for row in dummy.board:
					for square in row:
						if square != None and square.side == ('w' if queen.side == 'b' else 'b') and not isinstance(square, King):
							enemy_actions.extend(square.get_actions(dummy, checking_pins = True))
				
				if king.pos not in [move.end_pos for move in enemy_actions]:
					valid_moves.append(action)
			actions = valid_moves
		return actions
			
	def __str__(self):
		return 'q'

class Knight():
	def __init__(self, side, pos):
		self.side = side
		self.pos = pos

	def move(self, move, board):
		state = board.board
		pos = move.end_pos
		state[self.pos[0]][self.pos[1]] = None
		self.pos = pos
		state[pos[0]][pos[1]] = self 

		# Get the enemy kings position and see if hes in check
		king = get_king(side = 'w' if self.side == 'b' else 'b', board = state)
		actions = self.get_actions(board)
		if king.pos in [move.end_pos for move in actions]:
			king.check=True
		else:
			king.check = False

	def get_actions(self, board, checking_pins = False):
		actions = []
		x, y = self.pos
		offsets = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, -2), (1, 2), (2, 1), (2, -1)]
		for offset in offsets:
			if not x + offset[0] in [i for i in range(8)] or not y + offset[1] in [i for i in range(8)]:
				continue
			square = board.board[x+offset[0]][y+offset[1]]
			if square != None:
				if square.side != self.side:
					actions.append(Move(self, self.pos, (x+offset[0], y+offset[1])))
			else:
				actions.append(Move(self, self.pos, (x+offset[0], y+offset[1])))
		if not checking_pins:
			valid_moves = []
			for action in actions:
				# Create a deepcopy and get the queen
				dummy = deepcopy(board)
				knight = dummy.board[self.pos[0]][self.pos[1]]

				# Make the move
				move = Move(knight, knight.pos, action.end_pos)
				pos = move.end_pos
				dummy.board[self.pos[0]][self.pos[1]] = None
				knight.pos = pos
				dummy.board[pos[0]][pos[1]] = knight

				# Check if king is in check 
				king = get_king(side = self.side, board = dummy.board)
				enemy_actions = []
				for row in dummy.board:
					for square in row:
						if square != None and square.side == ('w' if knight.side == 'b' else 'b') and not isinstance(square, King):
							enemy_actions.extend(square.get_actions(dummy, checking_pins = True))
				
				if king.pos not in [move.end_pos for move in enemy_actions]:
					valid_moves.append(action)
			actions = valid_moves
		return actions

	def __str__(self):
		return 'n'

class Bishop():
	def __init__(self, side, pos):
		self.side = side
		self.pos = pos

	def move(self, move, board):
		state = board.board
		pos = move.end_pos
		state[self.pos[0]][self.pos[1]] = None
		self.pos = pos
		state[pos[0]][pos[1]] = self 
		# Get the enemy kings position and see if hes in check
		king = get_king(side = 'w' if self.side == 'b' else 'b', board = state)
		actions = self.get_actions(board)
		if king.pos in [move.end_pos for move in actions]:
			king.check=True
		else:
			king.check = False

	def get_actions(self, board, checking_pins = False):
		actions = get_diagonal(self, board)
		if actions == None:
			return []
		else:
			if not checking_pins:
				valid_moves = []
				for action in actions:
					# Create a deepcopy and get the queen
					dummy = deepcopy(board)
					bishop = dummy.board[self.pos[0]][self.pos[1]]

					# Make the move
					move = Move(bishop, bishop.pos, action.end_pos)
					pos = move.end_pos
					dummy.board[self.pos[0]][self.pos[1]] = None
					bishop.pos = pos
					dummy.board[pos[0]][pos[1]] = bishop

					# Check if king is in check 
					king = get_king(side = self.side, board = dummy.board)
					enemy_actions = []
					for row in dummy.board:
						for square in row:
							if square != None and square.side == ('w' if bishop.side == 'b' else 'b') and not isinstance(square, King):
								enemy_actions.extend(square.get_actions(dummy, checking_pins = True))
					
					if king.pos not in [move.end_pos for move in enemy_actions]:
						valid_moves.append(action)
				actions = valid_moves

			return actions
		
	def __str__(self):
		return 'b'

class Rook():
	def __init__(self, side, pos):
		self.side = side
		self.pos = pos
		self.moved = False
	
	def move(self, move, board):
		state = board.board
		pos = move.end_pos
		state[self.pos[0]][self.pos[1]] = None
		self.pos = pos
		state[pos[0]][pos[1]] = self
		self.moved = True

		# Get the enemy kings position and see if hes in check
		king = get_king(side = 'w' if self.side == 'b' else 'b', board = state)
		actions = self.get_actions(board)
		if king.pos in [move.end_pos for move in actions]:
			king.check=True
		else:
			king.check = False

	def get_actions(self, board, checking_pins = False):
		actions = []
		vert = get_vertical(self, board)
		horz = get_horizontal(self, board)
		if vert != None:
			actions.extend(vert)
		if horz != None:
			actions.extend(horz)
		if not checking_pins:
			valid_moves = []
			for action in actions:
				# Create a deepcopy and get the queen
				dummy = deepcopy(board)
				rook = dummy.board[self.pos[0]][self.pos[1]]

				# Make the move
				move = Move(rook, rook.pos, action.end_pos)
				pos = move.end_pos
				dummy.board[self.pos[0]][self.pos[1]] = None
				rook.pos = pos
				dummy.board[pos[0]][pos[1]] = rook

				# Check if king is in check 
				king = get_king(side = self.side, board = dummy.board)
				enemy_actions = []
				for row in dummy.board:
					for square in row:
						if square != None and square.side == ('w' if rook.side == 'b' else 'b') and not isinstance(square, King):
							enemy_actions.extend(square.get_actions(dummy, checking_pins = True))
				
				if king.pos not in [move.end_pos for move in enemy_actions]:
					valid_moves.append(action)
			actions = valid_moves
		return actions
		
	def __str__(self):
		return 'r'
		
class Pawn():
	def __init__(self, side, pos):
		self.side = side
		self.pos = pos
		self.first_move = False

	def move(self, move, board):
		state = board.board
		if abs(self.pos[0] - move.end_pos[0]) == 2:
			self.first_move = True
		else:
			self.first_move = False
		state[self.pos[0]][self.pos[1]] = None
		self.pos = move.end_pos

		match move.promoted_peice:
			case 'q':
				state[move.end_pos[0]][move.end_pos[1]] = Queen(side = self.side, pos = move.end_pos)
			case 'r':
				state[move.end_pos[0]][move.end_pos[1]] = Rook(side = self.side, pos = move.end_pos)
			case 'b':
				state[move.end_pos[0]][move.end_pos[1]] = Bishop(side = self.side, pos = move.end_pos)
			case 'n':
				state[move.end_pos[0]][move.end_pos[1]] = Knight(side = self.side, pos = move.end_pos)
			case _:
				state[move.end_pos[0]][move.end_pos[1]] = self 
		# Get the enemy kings position and see if hes in check
		king = get_king(side = 'w' if self.side == 'b' else 'b', board = state)
		actions = self.get_actions(board)
		if king.pos in [move.end_pos for move in actions]:
			king.check=True
		else:
			king.check = False
			
	def get_actions(self, board, checking_pins = False):
		actions = []
		x, y = self.pos

		# Multiplier for both sides
		mpl = 1 if self.side == 'w' else -1

		# Normal case
		if  0 <= x+(1*mpl) < 8:
			if board.board[x+(1*mpl)][y] == None:
				# Check if pawn is promoting
				if (x == 6 and self.side == 'w') or (x == 1 and self.side == 'b'):
					actions.append(Move(self, self.pos, (x+(1*mpl), y), 'q'))
					actions.append(Move(self, self.pos, (x+(1*mpl), y), 'n'))
					actions.append(Move(self, self.pos, (x+(1*mpl), y), 'b'))
					actions.append(Move(self, self.pos, (x+(1*mpl), y), 'r'))
				else:
					actions.append(Move(self, self.pos, (x+(1*mpl), y)))


		# First move 
		if (self.side == 'w' and x == 1) or (self.side == 'b' and x == 6):
			if board.board[x+(2*mpl)][y] == None and board.board[x+(1*mpl)][y] == None:
				actions.append(Move(self, self.pos, (x+(2*mpl), y)))

		# Captures
		for i in range(2):
			n = 1 if i == 0 else -1
			if 0 <= x+(1*mpl) < 8 and 0 <= y+n < 8:
				if board.board[x+(1*mpl)][y+n] != None:
					if board.board[x+(1*mpl)][y+n].side != self.side:
						if (x == 6 and self.side == 'w') or (x == 1 and self.side == 'b'):
							actions.append(Move(self, self.pos, (x+(1*mpl), y+n), 'q'))
							actions.append(Move(self, self.pos, (x+(1*mpl), y+n), 'n'))
							actions.append(Move(self, self.pos, (x+(1*mpl), y+n), 'b'))
							actions.append(Move(self, self.pos, (x+(1*mpl), y+n), 'r'))
						else:
							actions.append(Move(self, self.pos, (x+(1*mpl), y+n)))

		# En passant captures
		for i in range(2):
			n = 1 if i == 0 else -1
			if 0 <= x+(1*mpl) < 8 and 0 <= y+n < 8:
				if board.board[x+(1*mpl)][y+n] == None and isinstance(board.board[x][y+n], Pawn):
					if board.board[x][y+n].side != self.side and board.board[x][y+n].first_move == True:
						actions.append(Move(self, self.pos, (x+(1*mpl), y+n)))
		
		if not checking_pins:
			valid_moves = []
			for action in actions:
				# Create a deepcopy and get the queen
				dummy = deepcopy(board)
				pawn = dummy.board[self.pos[0]][self.pos[1]]

				# Make the move
				move = Move(pawn, pawn.pos, action.end_pos)
				pos = move.end_pos
				dummy.board[self.pos[0]][self.pos[1]] = None
				pawn.pos = pos
				dummy.board[pos[0]][pos[1]] = pawn

				# Check if king is in check 
				king = get_king(side = self.side, board = dummy.board)
				enemy_actions = []
				for row in dummy.board:
					for square in row:
						if square != None and square.side == ('w' if pawn.side == 'b' else 'b') and not isinstance(square, King):
							enemy_actions.extend(square.get_actions(dummy, checking_pins = True))
				
				if king.pos not in [move.end_pos for move in enemy_actions]:
					valid_moves.append(action)
			actions = valid_moves
		return actions

	def __str__(self):
		return 'p'

def get_king(side, board):
	for row in board:
		for sq in row:
			if isinstance(sq, King):
				if sq.side == side:
					return sq

def get_vertical(peice, board):
	board = board.board
	x, y = peice.pos
	actions = []
	for i in range(x+1, 8):
		if board[i][y] != None:
			if board[i][y].side != peice.side:
				actions.append(Move(peice, peice.pos, (i, y)))
			break
		actions.append(Move(peice, peice.pos, (i, y)))
	for i in [num for num in range(x)][::-1]:
		if board[i][y] != None:
			if board[i][y].side != peice.side:
				actions.append(Move(peice, peice.pos, (i, y)))
			break
		actions.append(Move(peice, peice.pos, (i, y)))
	return actions

def get_horizontal(peice, board):
	board = board.board
	x, y = peice.pos
	actions = []
	for i in range(y+1, 8):
		if board[x][i] != None:
			if board[x][i].side != peice.side:
				actions.append(Move(peice, peice.pos, (x, i)))
			break
		actions.append(Move(peice, peice.pos, (x, i)))
	for i in [j for j in range(y)][::-1]:
		if board[x][i] != None:
			if board[x][i].side != peice.side:
				actions.append(Move(peice, peice.pos, (x, i)))
			break
		actions.append(Move(peice, peice.pos, (x, i)))
	return actions

def get_diagonal(peice, board):
	board = board.board
	actions = []
	x, y = peice.pos
	i = 1
	while True:
		if not (x+i < 8 and y+i < 8):
			break
		if board[x+i][y+i] != None:
			if board[x+i][y+i].side != peice.side:
				actions.append(Move(peice, peice.pos, (x+i, y+i)))
			break
		actions.append(Move(peice, peice.pos, (x+i, y+i)))

		i+=1

	i= 1
	while True:
		if not (x-i >= 0 and y-i >= 0):
			break
		if board[x-i][y-i] != None:
			if board[x-i][y-i].side != peice.side:
				actions.append(Move(peice, peice.pos, (x-i, y-i)))
			break
		actions.append(Move(peice, peice.pos, (x-i, y-i)))

		i+=1
	i=1
	while True:
		if not (x-i >= 0 and y+i < 8):
			break
		if board[x-i][y+i] != None:
			if board[x-i][y+i].side != peice.side:
				actions.append(Move(peice, peice.pos, (x-i, y+i)))
			break
		actions.append(Move(peice, peice.pos, (x-i, y+i)))

		i+=1
	i=1
	while True:
		if not (x+i < 8 and y-i >= 0):
			break
		if board[x+i][y-i] != None:
			if board[x+i][y-i].side != peice.side:
				actions.append(Move(peice, peice.pos, (x+i, y-i)))
			break
		actions.append(Move(peice, peice.pos, (x+i, y-i)))

		i+=1
	return actions