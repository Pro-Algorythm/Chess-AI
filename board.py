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
                    if j.side == side:
                        actions = j.get_actions(self.board)
                        if len(actions) != 0:
                            print([(move.start_pos, move.end_pos, str(move.peice)) for move in actions])
                            moves.extend(actions)
        return moves

    def is_valid(board):
        # STILL NEEDS WORK ----> HOW TO TELL IF A POSITION IS VALID?
        if len(board) != 8 or len([True for row in board if len(row) == 8]) != 8:
            return False
        white_pieces = dict([(piece, 0) for piece in ['k','q','r','n','bb','wb','p']])
        black_pieces = dict([(piece, 0) for piece in ['k','q','r','n','bb','wb','p']])
        for row in board:
            for square in row:
                match square:
                    case 'wk':
                        white_pieces['k']+=1
                    case 'wq':
                        white_pieces['q']+=1
                    case 'wn':
                        white_pieces['n']+=1
                    case 'wwb':
                        white_pieces['wb']+=1
                    case 'wbb':
                        white_pieces['wbb']+=1
                    case 'wp':
                        white_pieces['p']+=1
                    case 'bk':
                        black_pieces['k']+=1
                    case 'bq':
                        black_pieces['q']+=1
                    case 'bn':
                        black_pieces['n']+=1
                    case 'bwb':
                        black_pieces['wb']+=1
                    case 'bbb':
                        black_pieces['wbb']+=1
                    case 'bp':
                        black_pieces['p']+=1
                    case _:
                        pass
        
        if white_pieces['k'] != 1 or black_pieces['k'] != 1:
            return False
        return True
    
    def is_terminal(self):
        # TODO: Return a boolean indicating whether the board is terminal or not.

        # Check if white is in checkmate

        pass

    def get_util(self):
        # TODO: Return the evalutaion of the board
        pass

    def get_material(self, side):
        # TODO: Return the value of the material for the specified side
        pass

    def __str__(self):
        board = self.board
        return tabulate.tabulate(board, tablefmt = 'grid')
