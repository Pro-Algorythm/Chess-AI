from pieces import *
import tabulate

class Board():
    def __init__(self):
        # Create a new board
        board = []

        # Define empty
        empty = None

        # Create black and whites main pieces first
        for i in range(2):
            if i == 0:
                side = 'w'
            else:
                side = 'b'
            row = []
            row.append(Rook(side=side, pos = (0,0) if i == 0 else (7,0)))
            row.append(Knight(side=side, pos = (0,1) if i == 0 else (7,1)))
            row.append(Bishop(side=side, pos = (0,2) if i == 0 else (7,2)))
            row.append(Queen(side=side, pos = (0, 3) if i == 0 else (7, 3)))
            row.append(King(side=side))
            row.append(Bishop(side=side, pos = (0,5) if i == 0 else (7,5)))
            row.append(Knight(side=side, pos = (0,6) if i == 0 else (7,6)))
            row.append(Rook(side=side, pos = (0,7) if i == 0 else (7,7)))
            if i == 0:
                white_row1 = row
            else:
                black_row1 = row

        # Set the white pieces
        board.append(white_row1)
        board.append([Pawn(side='w', pos = (1, i)) for i in range(8)])

        # Set the empty squares in the middle
        for i in range(4):
            board.append([empty for i in range(8)])
        
        
        # Set the black pieces
        board.append([Pawn(side='b', pos = (6, i)) for i in range(8)])
        board.append(black_row1)

        # Set the board
        self.board = board
         
    def get_all_actions(self, side):
        # Initialize moves array
        moves = []

        # Loop through the whole board storing all actions of a side
        for i in self.board:
            for j in i:
                if j != None:
                    if j.side == side and not isinstance(j, King):
                        actions = j.get_actions(self)
                        if len(actions) != 0:
                            moves.extend(actions)

        return moves

    def is_terminal(self):
        # Get the kings
        for row in self.board:
            for square in row:
                if square != None and isinstance(square, King):
                    if square.side == 'w': white_king = square
                    else: black_king = square
                
        # Get both players actions
        white_actions = len(self.get_all_actions(side = 'w'))
        black_actions = len(self.get_all_actions(side = 'b'))

        # Check for all results
        if white_actions == 0 and not white_king.check:
            return 0
        elif white_actions == 0 and white_king.check:
            return float('inf')
        elif black_actions == 0 and not black_king.check:
            return 0
        elif black_actions == 0 and black_king.check:
            return float('-inf')
        else:
            return False

    def get_util(self):
        # Get the material of both sides
        white_material = self.get_material(side = 'w')
        black_material = self.get_material(side = 'b')

        # Caclulate their space/control in enemys side
        white_actions = self.get_all_actions(side = 'w')
        black_actions = self.get_all_actions(side = 'b')

        white_space = 0
        for action in white_actions:
            if action.end_pos[0] > 3:
                white_space += 1
        black_space = 0
        for action in black_actions:
            if action.end_pos[0] < 4:
                black_space += 1

        # Get the evaluation and return it
        eval = (white_material + white_space*0.5) - (black_material - black_space*0.5)
        return eval
    
    def get_material(self, side):
        pawn_pst = [
            [0 for i in range(8)],
            [0, 0, -0.5, -1, -1, -0.5, 0, 0],
            [0.5, 0.5, 0.75, 0.75, 0.75, 0.75, 0.5, 0.5],
            [0.5, 0.5, 1, 2, 2, 1, 0.5, 0.5],
            [0.5, 1, 2, 2, 2, 2, 1, 0.5],
            [1, 1, 2.25, 2.25, 2.25, 2.25, 1, 1],
            [2, 2, 2.75, 2.75, 2.75, 2.75, 2, 2],
            [10 for i in range(8)]
        ]

        knight_pst = [
            [0 for i in range(8)],
            [-1, -0.5, 0.75, 0.75, 0.75, 0.75, -0.5, -1],
            [-1.25, 1.5, 1.75, 1.75, 1.75, 1.75, 1.5, -1.25],
            [-2.25, 2.5, 5, 5, 5, 5, 2.5, -2.25],
            [-2.25, 2.5, 5, 5, 5, 5, 2.5, -2.25],
            [-1.25, 1.5, 1.75, 1.75, 1.75, 1.75, 1.5, -1.25],
            [-1, 0.5, 0.75, 0.75, 0.75, 0.75, 0.5, -1],
            [-1, 0.5, 0.75, 0.75, 0.75, 0.75, 0.5, -1],
        ]

        bishop_pst = [
            [-1 for i in range(8)],
            [-0.5, 3, 1, 1, 1, 1, 3, -0.5],
            [-0.5, 1, 3, 1, 1, 3, 1, -0.5],
            [-0.5, 1, 3, 1, 1, 3, 1, -0.5],
            [-0.5, 1, 3, 1, 1, 3, 1, -0.5],
            [-0.5, 1, 3, 1, 1, 3, 1, -0.5],
            [-0.5, 1, 3, 1, 1, 3, 1, -0.5],
            [-1 for i in range(8)],
        ]

        king_pst = [
            [3, 3, 3, 5, -2, 3, 5, 3],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [-1 for i in range(8)],
            [-1 for i in range(8)],
            [-1 for i in range(8)],
            [-1 for i in range(8)],
            [-1 for i in range(8)],
            [0 for i in range(8)]
        ]

        # Flip the PST's for black
        if side == 'b':
            king_pst = king_pst[::-1]
            bishop_pst = bishop_pst[::-1]
            knight_pst = knight_pst[::-1]
            pawn_pst = pawn_pst[::-1]

        material = 0
        for row in self.board:
            for sq in row:
                if sq != None:
                    if sq.side == side:
                        if isinstance(sq, Queen): material+=9
                        if isinstance(sq, Rook): material+=5
                        if isinstance(sq, Knight): material+= 3 + knight_pst[sq.pos[0]][sq.pos[1]]
                        if isinstance(sq, Bishop): material+= 3 + bishop_pst[sq.pos[0]][sq.pos[1]]
                        if isinstance(sq, Pawn): material+= 1 + pawn_pst[sq.pos[0]][sq.pos[1]]
        return material

    def __str__(self):
        board = self.board
        return tabulate.tabulate(board, tablefmt = 'grid')
