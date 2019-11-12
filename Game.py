def game_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])


# test_board =['','1','2','3','4','5','6','7','8','9']
# game_board(test_board)

def player_input():
    marker = input("Enter the player input X or O: ")
    if marker.lower() == 'x':
        return ('x','o')
    else:
        return ('o', 'x')

def place_marker(board,marker,position):
    board[position] = marker


def win_check (board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

import random
def choose_first():
   if  random.randint(0,1) == 0:
       return 'Player 1'
   else:
       return 'Player 2'

def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range (0,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Enter the choice between(1-9): "))
    return position

def replay():
    return input("Do you want to play the game again? Enter Yes or No: ").lower().startswith('y')

print ("Welcome to TIC TAC TOE game")
while True:
    test_board = [' '] * 10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print (turn + ' will go first...')
    play_game = input("Are you ready to start the game ? Enter Yes or No..")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            game_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board,player1_marker,position)
            if win_check(test_board,player1_marker):
                game_board(test_board)
                print("Congratulations Player1 won the game!!!!")
                game_on = False
            else:
                if full_board_check(test_board):
                    game_board(test_board)
                    print ("The Game is tie...")
                    break
                else:
                    turn = 'Player 2'
        else:
            game_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board,player2_marker, position)
            if win_check(test_board,player2_marker):
                game_board(test_board)
                print("Congratulations Player2 won the game!!!!")
                game_on = False
            else:
                if full_board_check(test_board):
                    game_board(test_board)
                    print("The Game is tie...")
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break