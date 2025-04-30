from board import *

def test_init():
    board = Board()
    assert all(peice.side == 'w' for peice in board.board[0]) and all(peice.side == 'w' and isinstance(peice, Pawn) for peice in board.board[1])
    assert all(peice.side == 'b' and isinstance(peice, Pawn) for peice in board.board[6]) and all(peice.side == 'b' for peice in board.board[7])

def test_first_moves():
    board = Board()
    assert len(board.get_all_actions(side = 'w')) == 20 and len(board.get_all_actions(side = 'b')) == 20

def test_is_terminal():
    board = Board()
    assert not board.is_terminal()

def test_get_util():
    board = Board()
    assert board.get_util() == 0

def test_get_material():
    board=  Board()
    assert all(board.get_material(side = side) == 39 for side in ['w', 'b'])