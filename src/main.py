from board import *
from argparse import ArgumentParser
import pygame as pg

def main():
    parser = ArgumentParser()
    parser.add_argument('-u', '--gui', action = 'store_true')
    args = parser.parse_args()
    gui = args.gui
    turn = 'w'

    board = Board()

    if not gui:
        player = input("Play as black (b) or white (w): ")
        ai = 'w' if player == 'b' else 'b'

        while True:
            terminality = board.is_terminal(turn = turn)
            if terminality:
                if terminality == player:
                    print("You won.")
                    exit()
                elif terminality == ai:
                    print("You lost, the AI won.")
                    exit()
                else:
                    print("Its a draw by stalemate.")
                    exit()
            if player == turn:
                print(board)
                move = input('Enter move as (peice end_pos promotion(if applicable) castling(if applicable)): ')
                paras = move.split()
                peice, end_pos = paras[0], paras[1]
                if len(paras) == 3:
                    if paras[2] in ['kingside', 'queenside']:
                        castling = paras[2]
                        promotion = None
                    else:
                        promotion = paras[2]
                        castling = None
                elif len(paras) == 4:
                    promotion = paras[2]
                    castling = paras[3]
                else:
                    promotion = None
                    castling = None
                peice = board.board[int(peice[1])][int(peice[3])]
                move = Move(peice, peice.pos, (int(end_pos[1]), int(end_pos[3])), promoted_peice = promotion, castling = castling)
            
            else:
                global depth
                depth = 10
                move = get_best_move(board, turn)[0]
            
            # Make the move and update the turn
            move.peice.move(move, board)
            turn = 'w' if turn == 'b' else 'b'
    
    else:
        # Initialize the window
        pg.init()
        window = pg.display.set_mode((700,500))

        # Load all peices
        b_pawn = pg.image.load('../assets/black_pawn.png')
        w_pawn = pg.image.load('../assets/white_pawn.png')
        b_king = pg.image.load('../assets/black_king.png')
        w_king = pg.image.load('../assets/white_king.png')
        b_queen = pg.image.load('../assets/black_queen.png')
        w_queen = pg.image.load('../assets/white_queen.png')
        b_bishop = pg.image.load('../assets/black_bishop.png')
        w_bishop = pg.image.load('../assets/white_bishop.png')
        b_knight = pg.image.load('../assets/black_knight.png')
        w_knight = pg.image.load('../assets/white_knight.png')
        b_rook = pg.image.load('../assets/black_rook.png')
        w_rook = pg.image.load('../assets/white_rook.png')

        start_pos = None
        end_pos = None
        
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                        running = False
            
            # Set the board
            for i in range(8):
                for j in range(8):
                    colour = (200, 200, 200) if (i+j)%2 != 0 else (100, 100, 100)
                    rect = pg.Rect(150+(50*i), 50+(50*j), 50, 50)
                    pg.draw.rect(window, colour, rect)
                    if board.board[j][i] != None:
                        if board.board[j][i].side == 'b':
                            match str(board.board[j][i]):
                                case 'r':
                                    window.blit(b_rook, (144+(50*i), 45+(50*j)))
                                case 'n':
                                    window.blit(b_knight, (144+(50*i), 45+(50*j)))
                                case 'b':
                                    window.blit(b_bishop, (144+(50*i), 45+(50*j)))
                                case 'q':
                                    window.blit(b_queen, (144+(50*i), 45+(50*j)))
                                case 'k':
                                    window.blit(b_king, (144+(50*i), 45+(50*j)))
                                case 'p':
                                    window.blit(b_pawn, (144+(50*i), 45+(50*j)))
                        else:
                            match str(board.board[j][i]):
                                case 'r':
                                    window.blit(w_rook, (144+(50*i), 45+(50*j)))
                                case 'n':
                                    window.blit(w_knight, (144+(50*i), 45+(50*j)))
                                case 'b':
                                    window.blit(w_bishop, (144+(50*i), 45+(50*j)))
                                case 'q':
                                    window.blit(w_queen, (144+(50*i), 45+(50*j)))
                                case 'k':
                                    window.blit(w_king, (144+(50*i), 45+(50*j)))
                                case 'p':
                                    window.blit(w_pawn, (144+(50*i), 45+(50*j)))
            pg.display.update()

            terminality = board.is_terminal(turn = turn)
            if terminality == 'w':
                print("You Won.")
                break
            if terminality == 'b':
                print("AI won")
                break

            if turn == 'w':
                # For now player is always white
                for event in pg.event.get():
                    if event.type == pg.MOUSEBUTTONDOWN:
                        x, y = pg.mouse.get_pos()
                        if not (150 <= x <= 550 and 50 <= y <= 450):
                            start_pos = None
                            end_pos = None
                            break

                        x, y = int((y-50) / 50), int((x-150) / 50)
                        if board.board[x][y] == None and start_pos == None:
                            continue
                        if start_pos != None:
                            end_pos = (x, y)
                        else:
                            start_pos = (x, y)
                
                if end_pos:
                    # Set castle value
                    castle = None
                    if isinstance(board.board[start_pos[0]][start_pos[1]], King):
                        if end_pos[1] - start_pos[1] > 1:
                            castle = 'kingside' if end_pos[1] > start_pos[1] else 'queenside'
                    
                    # For now all promotions are queens
                    if isinstance(board.board[start_pos[0]][start_pos[1]], Pawn):
                        if (board.board[start_pos[0]][start_pos[1]].side == 'w' and end_pos[0] == 7) or (board.board[start_pos[0]][start_pos[1]].side == 'b' and end_pos[0] == 1):
                            promotion = 'q'

                    promotion = None
                    # Make the move object
                    move = Move(board.board[start_pos[0]][start_pos[1]], start_pos, end_pos, promoted_peice = promotion, castling = castle)
                    # Reset the variables
                    start_pos = None
                    end_pos = None

                    # See if the action is valid
                    actions = board.get_all_actions(side = turn, include_king = True)
                    if (move.start_pos, move.end_pos, move.promoted_peice, move.castling) in [(action.start_pos, action.end_pos, action.promoted_peice, action.castling) for action in actions]:
                        board.board[move.start_pos[0]][move.start_pos[1]].move(move, board)
                        turn = 'w' if turn == 'b' else 'b'

            else:
                depth = 10
                move = get_best_move(board, turn = turn)[0]
                board.board[move.start_pos[0]][move.start_pos[1]].move(move, board)
                turn = 'w' if turn == 'b' else 'b'                     

def get_best_move(board, turn, alpha = None):
    global depth
    depth -= 1
    actions = board.get_all_actions(side = turn)

    best_move = None
    for action in actions:
        dummy = deepcopy(board)
        peice = dummy.board[action.start_pos[0]][action.start_pos[1]]
        peice.move(action, dummy)
        terminality = dummy.is_terminal(turn = turn)

        if terminality != False:
            eval = float('inf') if terminality == 'w' else (float('-inf') if terminality == 'b' else 0)
        else:
            eval = dummy.get_util()

        if (turn == 'w' and eval == float('inf')) or (turn == 'b' and eval == float('-inf')):
            return (action, eval)
        elif not (turn == 'w' and eval == float('inf')) or not (turn == 'b' and eval == float('-inf')):
            if best_move == None:
                best_move = (action, eval)
        else:
            if not depth <= 0:
                move = (action, get_best_move(dummy, turn = 'w' if turn == 'b' else 'b', alpha = alpha)[1])
            else:
                if terminality == 0:
                    move = (action, eval)
                else:
                    move = (action, eval)
        
            if best_move == None or ((eval > float(best_move[1]) and turn == 'w') or (eval < float(best_move[1]) and turn == 'b')):
                best_move = move

        if alpha != None:
            if (eval < alpha and turn == 'b') or (eval > alpha and turn == 'w'):
                return (action, eval)
        alpha = best_move[1]
    
    return best_move


if __name__ == '__main__':
    main()