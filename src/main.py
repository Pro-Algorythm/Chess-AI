from pieces import *
from board import *
import copy

board = Board()
king = board.board[0][4]
pawn = board.board[1][3]
black_bishop = board.board[7][2]




pawn_actions = pawn.get_actions(board)

pawn.move(pawn_actions[1], board)

black_bishop.move(Move(black_bishop, black_bishop.pos, (2,2)), board)

king_actions = king.get_actions(board)
all_actions = board.get_all_actions(side = 'w')



print(len(all_actions), *[str(move) for move in all_actions])
print(board.board[1][3])

print(board)

print(king.pos, king.side, king.check)

black_bishop.move(Move(black_bishop, black_bishop.pos, (3,3)), board)
print(board)
print(king.pos, king.check)