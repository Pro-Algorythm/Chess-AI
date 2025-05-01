from board import *
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('-u', '--gui', action = 'store_true')
    args = parser.parse_args()
    gui = args.gui

    board = Board()
    if not gui:
        player = input("Play as black (b) or white (w): ")
    else:
        pass
    ai = 'w' if player == 'b' else 'b'
    turn = 'w'

    while True:
        terminality = board.is_terminal()
        if terminality:
            if terminality == player:
                if not gui:
                    print("You won.")
                    exit()
                else:
                    pass
            elif terminality == ai:
                if not gui:
                    print("You lost, the AI won.")
                    exit()
                else:
                    pass
            else:
                if not gui:
                    print("Its a draw by stalemate.")
                    exit()
                else:
                    pass
        if player == turn:
            if not gui:
                print(board)
                move = input('Enter move as (peice end_pos promotion(if applicable) castling(if applicable)): ')
                peice, end_pos, promotion, castling = move.split()
                if promotion == 'None':
                    promotion = None
                if castling == 'None':
                    castling = None
                peice = board.board[int(peice[1])][int(peice[3])]
                move = Move(peice, peice.pos, (int(end_pos[1]), int(end_pos[3])), promoted_peice = promotion, castling = castling)
            else:
                pass

        else:
            global depth
            depth = 10
            move = get_best_move(board, turn)[0]
        
        # Make the move and update the turn
        move.peice.move(move, board)
        turn = 'w' if turn == 'b' else 'b'


def get_best_move(board, turn):
    global depth
    depth -= 1
    actions = board.get_all_actions(side = turn)
    
    best_move = None
    for action in actions:
        dummy = deepcopy(board)
        peice = dummy.board[action.start_pos[0]][action.start_pos[1]]
        peice.move(action, dummy)
        terminality = dummy.is_terminal()
        eval = dummy.get_util()
        if terminality != False:
            if terminality == (float('inf') if turn == 'w' else float('-inf')):
                return (action, terminality)
            else:
                if best_move == None or ((best_move[1] < 0 and turn == 'b') or (best_move[1] > 0 and turn == 'w')):
                    best_move = (action, terminality)
        if not depth <= 0:
            move = get_best_move(dummy, turn = 'w' if turn == 'b' else 'b')
        else:
            move = (action, eval)

        if best_move == None or ((eval > best_move[1] and turn == 'w') or (eval < best_move[1] and turn == 'b')):
            best_move = move
    return best_move
        
if __name__ == '__main__':
    main()