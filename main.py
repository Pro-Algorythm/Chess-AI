from pieces import *
from board import *
import copy
import tabulate
# bLack pawn has side of white
board = Board()
state = copy.deepcopy(board.board)

state[0][1] = None
index1_dict = 'abcdefgh'


print(board)
print([move.end_pos for move in actions])
print(len(actions))



