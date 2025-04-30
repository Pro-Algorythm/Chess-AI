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
        moves = []
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
            return 'stalemate'
        elif white_actions == 0 and white_king.check:
            return 'white'
        elif black_actions == 0 and not black_king.check:
            return 'stalemate'
        elif black_actions == 0 and black_king.check:
            return 'white'
        else:
            return False

    def get_util(self):
        eval = self.get_material(side = 'w') - self.get_material(side = 'b')
        return eval
    
    def get_material(self, side):
        # TODO: Return the value of the material for the specified side
        material = 0
        for row in self.board:
            for sq in row:
                if sq != None:
                    if sq.side == side:
                        if isinstance(sq, Queen): material+=9
                        if isinstance(sq, Rook): material+=5
                        if isinstance(sq, Knight) or isinstance(sq, Bishop): material+=3
                        if isinstance(sq, Pawn): material+=1
        return material

    def __str__(self):
        board = self.board
        return tabulate.tabulate(board, tablefmt = 'grid')
