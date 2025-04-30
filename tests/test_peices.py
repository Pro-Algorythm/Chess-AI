from pieces import *
from board import *

def test_king():
    board = Board()
    king = board.board[0][4]

    # Check for initial side, position and actions
    assert king.pos == (0, 4)
    assert king.side == 'w'
    assert len(king.get_actions(board)) == 0

    # Check for normal actions
    pawn = board.board[1][4]
    pawn.move(Move(pawn, pawn.pos, (3, 4)), board)
    board.board[1][3].move(Move(board.board[1][3], board.board[1][3].pos, (3, 3)), board)
    assert len(king.get_actions(board)) == 2

    # Check kings action if there are none due to check
    bishop = board.board[7][2]
    bishop.move(Move(bishop, bishop.pos, (3, 1)), board)
    assert len(king.get_actions(board)) == 1

def test_king_castle():
    # Check for kingside castling
    board = Board()
    king = board.board[0][4]
    pawn = board.board[1][4]
    bishop = board.board[0][5]
    knight = board.board[0][6]
    kingside_rook = board.board[0][7]
    print(king.check)
    pawn.move(Move(pawn, pawn.pos, (3, 4)), board)
    bishop.move(Move(bishop, bishop.pos, (3, 2)), board)
    knight.move(Move(knight, knight.pos, (2, 5)), board)


    actions = king.get_actions(board)
    castle_move = [move for move in actions if move.castling == 'kingside'][0]
    assert len(actions) == 3
    assert any(action.end_pos == (0, 6) for action in actions)
    king.move(castle_move, board)
    assert king.pos == (0, 6) and kingside_rook.pos == (0, 5)

def test_queen():
    # Check initial board
    board = Board()
    queen = board.board[0][3]
    assert len(queen.get_actions(board)) == 0

    pawn = board.board[1][3]
    pawn.move(Move(pawn, pawn.pos, (3,3)), board)

    # Checking check detection
    bishop = board.board[7][2]
    bishop.move(Move(bishop, bishop.pos, (3, 1)),board)
    king = board.board[0][4]
    assert king.check
    assert len(queen.get_actions(board)) == 1

    # Checking queens moves when its pinned
    queen.move(queen.get_actions(board)[0], board)
    assert len(queen.get_actions(board)) == 2

    # Check queens moves when king is in check and queen cant do anything
    queen.move(Move(queen, queen.pos, (4,4)), board)
    assert len(queen.get_actions(board)) == 0

    # Check the queens normal moves
    bishop.move(Move(bishop, bishop.pos, (7,2)), board)
    print(board)
    assert len(queen.get_actions(board)) == 17

def test_knight():
    board = Board()
    king = board.board[0][4]
    knight = board.board[0][1]
    # Check for moves in init board
    assert len(knight.get_actions(board)) == 2

    # Check for other moves
    pawn = board.board[1][3]
    pawn.move(Move(pawn, pawn.pos, (3,3)), board)
    assert len(knight.get_actions(board)) == 3

    # Check for moves in check
    bishop = board.board[7][2]
    bishop.move(Move(bishop, bishop.pos, (2,2)), board)
    assert king.check
    assert len(knight.get_actions(board)) == 2

    # Check for moves in pin
    knight.move(Move(knight, knight.pos, (1, 3)), board)
    assert len(knight.get_actions(board)) == 0

    # Check for normal moves
    bishop.move(Move(bishop, bishop.pos, (7, 2)), board)
    knight.move(Move(knight, knight.pos, (3, 4)), board)
    print(board)
    assert len(knight.get_actions(board)) == 7
    
def test_bishop():
    board = Board()
    king = board.board[0][4]
    # Right bishop
    bishop = board.board[0][5]
    assert len(bishop.get_actions(board)) == 0
    pawn = board.board[1][4]
    pawn.move(Move(pawn, pawn.pos, (3, 4)), board)
    assert len(bishop.get_actions(board)) == 5

    # Check for pins
    bishop.move(Move(bishop, bishop.pos, (1, 4)), board)
    
    enemy_queen = board.board[7][3]
    enemy_queen.move(Move(enemy_queen, enemy_queen.pos, (3, 4)), board)
    assert not king.check
    assert len(bishop.get_actions(board)) == 0

    bishop.move(Move(bishop, bishop.pos, end_pos = (0, 5)), board)
    assert len(bishop.get_actions(board)) == 1

def test_rook():
    board = Board()
    rook = board.board[0][0]
    assert len(rook.get_actions(board)) == 0

    # Cecking pins
    board.board[1][4] = None
    board.board[7][3].move(Move(board.board[7][3], board.board[7][3].pos, (3, 4)), board)
    rook.move(Move(rook, rook.pos, (1, 4)), board)
    assert len(rook.get_actions(board)) == 2

def test_pawns():
    board = Board()
    pawn = board.board[1][3]
    # Normal moves + First move
    assert len(pawn.get_actions(board)) == 2

    # Captures
    queen = board.board[7][3]
    queen.move(Move(queen, queen.pos, (2, 4)), board)
    assert len(pawn.get_actions(board)) == 3

    # En-Passant
    pawn.move(Move(pawn, pawn.pos, (4, 3)), board)
    board.board[6][4].move(Move(board.board[6][4], board.board[6][4].pos, (4,4)), board)
    assert len(pawn.get_actions(board)) == 2

    # Promotion
    board.board[7][0] = None
    pawn.move(Move(pawn, pawn.pos, (6, 0)), board)
    assert len(pawn.get_actions(board)) == 8