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
         
    def get_all_actions(self, side, include_king = False):
        # Initialize moves array
        moves = []

        # Loop through the whole board storing all actions of a side
        for row in self.board:
            for square in row:
                if square != None:
                    if square.side == side and (include_king or (not include_king and not isinstance(square, King))):
                        actions = square.get_actions(self)
                        if len(actions) != 0:
                            moves.extend(actions)

        return moves

    def is_terminal(self, turn):
        # Get the kings
        for row in self.board:
            for square in row:
                if square != None and isinstance(square, King):
                    if square.side == 'w': white_king = square
                    else: black_king = square
            
        actions = self.get_all_actions(side = 'w', include_king = True) if turn == 'w' else self.get_all_actions(side = 'b', include_king = True)
        # Check for checkmate
        if len(actions) == 0 and (white_king.check and turn == 'w'):
            return 'b'
        elif len(actions) == 0 and (black_king.check and turn == 'b'):
            return 'w'
        
        # Get actions for the side

        # Check for stalemate
        if len(actions) == 0:
            return 'stalemate'
        
        # Return false if board is not terminal
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
        
        eval = (white_material + white_space*0.25) - (black_material + black_space*0.25)

        print(self)
        print(f"White material: {white_material}   Black material: {black_material}")
        print(f"White space: {white_space*0.25}  Black space: {black_space*0.25}")
        print(f"Total evaluation: {eval}")

        return eval
    
    def get_material(self, side):
        pawn_pst = [
            [0,   0,   0,   0,   0,   0,   0,   0],     # Rank 1 (index 0)
            [5,  10, 10,  20,  20, 10, 10,  5],         # Rank 2
            [5,  10, 15,  25,  25, 15, 10,  5],         # Rank 3
            [10, 20, 20,  30,  30, 20, 20, 10],         # Rank 4
            [20, 30, 30,  40,  40, 30, 30, 20],         # Rank 5
            [30, 40, 40,  50,  50, 40, 40, 30],         # Rank 6
            [40, 50, 50,  60,  60, 50, 50, 40],         # Rank 7
            [100, 100, 100, 100, 100,  100,  100,  100],         # Rank 8 (index 7, promotion rank)
        ]


        knight_pst = [
            [-50, -40, -30, -30, -30, -30, -40, -50],
            [-40, -20,   0,   5,   5,   0, -20, -40],
            [-30,   5,  10,  15,  15,  10,   5, -30],
            [-30,   0,  15,  20,  20,  15,   0, -30],
            [-30,   5,  15,  20,  20,  15,   5, -30],
            [-30,   0,  10,  15,  15,  10,   0, -30],
            [-40, -20,   0,   0,   0,   0, -20, -40],
            [-50, -40, -30, -30, -30, -30, -40, -50],
        ]


        bishop_pst = [
            [-20, -10, -10, -10, -10, -10, -10, -20],
            [-10,   5,   0,   0,   0,   0,   5, -10],
            [-10,  10,  10,  10,  10,  10,  10, -10],
            [-10,   0,  10,  10,  10,  10,   0, -10],
            [-10,   5,   5,  10,  10,   5,   5, -10],
            [-10,   0,   5,  10,  10,   5,   0, -10],
            [-10,   0,   0,   0,   0,   0,   0, -10],
            [-20, -10, -10, -10, -10, -10, -10, -20],
        ]


        king_pst = [
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-20, -30, -30, -40, -40, -30, -30, -20],
            [-10, -20, -20, -20, -20, -20, -20, -10],
            [20,  20,   0,   0,   0,   0,  20,  20],
            [20,  30,  10,   0,   0,  10,  30,  20],
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
                        if isinstance(sq, Knight): material+= 3
                        if isinstance(sq, Bishop): material+= 3
                        if isinstance(sq, Pawn): material+= 1
        if material <= 14:
            king_pst = [
                [-50, -40, -30, -20, -20, -30, -40, -50],
                [-30, -20, -10,   0,   0, -10, -20, -30],
                [-30, -10,  20,  30,  30,  20, -10, -30],
                [-30, -10,  30,  40,  40,  30, -10, -30],
                [-30, -10,  30,  40,  40,  30, -10, -30],
                [-30, -10,  20,  30,  30,  20, -10, -30],
                [-30, -30,   0,   0,   0,   0, -30, -30],
                [-50, -30, -30, -30, -30, -30, -30, -50],
            ]
        material = 0
        for row in self.board:
            for sq in row:
                if sq != None:
                    if sq.side == side:
                        if isinstance(sq, Queen): material+=9
                        if isinstance(sq, Rook): material+=5
                        if isinstance(sq, Knight): material+= 3 + knight_pst[sq.pos[0]][sq.pos[1]]*0.01
                        if isinstance(sq, Bishop): material+= 3 + bishop_pst[sq.pos[0]][sq.pos[1]]*0.01
                        if isinstance(sq, Pawn): material+= 1 + pawn_pst[sq.pos[0]][sq.pos[1]]*0.01
                        if isinstance(sq, King): material+= king_pst[sq.pos[0]][sq.pos[1]]
        return material

    def __str__(self):
        board = self.board
        return tabulate.tabulate(board, tablefmt = 'grid')
