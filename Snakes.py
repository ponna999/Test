import random
def snake_board(board):
    print('-----------------------------')
    print(board[100] + '|' + board[99] + '|' + board[98] + '|' + board[97] + '|' + board[96] + '|' + board[95] + '|' +
          board[94] + '|' + board[93] + '|' + board[92] + '|' + board[91])
    print('-----------------------------')
    print(board[81] + '|' + board[82] + '|' + board[83] + '|' + board[84] + '|' + board[85] + '|' + board[86] + '|' +
          board[87] + '|' + board[88] + '|' + board[89] + '|' + board[90])
    print('-----------------------------')
    print(board[80] + '|' + board[79] + '|' + board[78] + '|' + board[77] + '|' + board[76] + '|' + board[75] + '|' +
          board[74] + '|' + board[73] + '|' + board[72] + '|' + board[71])
    print('-----------------------------')
    print(board[61] + '|' + board[62] + '|' + board[63] + '|' + board[64] + '|' + board[65] + '|' + board[66] + '|' +
          board[67] + '|' + board[68] + '|' + board[69] + '|' + board[70])
    print('-----------------------------')
    print(board[60] + '|' + board[59] + '|' + board[58] + '|' + board[57] + '|' + board[56] + '|' + board[55] + '|' +
          board[54] + '|' + board[53] + '|' + board[52] + '|' + board[51])
    print('-----------------------------')
    print(board[41] + '|' + board[42] + '|' + board[43] + '|' + board[44] + '|' + board[45] + '|' + board[46] + '|' + board[47] + '|' + board[48] + '|' + board[49] + '|' + board[50])
    print('-----------------------------')
    print(board[40] + '|' + board[39] + '|' + board[38] + '|' + board[37] + '|' + board[36] + '|' + board[35] + '|' + board[34] + '|' + board[33] + '|' + board[32] + '|' + board[31])
    print('-----------------------------')
    print(board[21] + '|' + board[22] + '|' + board[23] + '|' + board[24] + '|' + board[25] + '|' + board[26] + '|' + board[27] + '|' + board[28] + '|' + board[29] + '|' + board[30])
    print('-----------------------------')
    print(board[20] + '|' + board[19] + '|' + board[18] + '|' + board[17] + '|' + board[16] + '|' + board[15] + '|' + board[14] + '|' + board[13] + '|' + board[12] + '|' + board[11])
    print('-----------------------------')
    print(board[1] +' |' + board[2] + ' |' + board[3] + ' |' + board[4] + ' |' + board[5] + ' |' + board[6] + ' |' + board[7] + ' |' + board[8] + ' |' + board[9] + ' |' + board[10])
    print('-----------------------------')


def game_board():
    test_board = []
    for i in range (0,101):
        test_board.append(str(i))
    return test_board

def player_marker():
    marker = input("Choose the symbol either * or @: ")
    if marker == '*':
        return ('*','@')
    else:
        return ('@','*')

def choose_first():
    if random.randint(0,1) == 1:
        return 'Player 1'
    else:
        return 'Player 2'
def check_win(board,mark):
    return board[100] =='100'+mark

def roll_dice():
    num = random.randint(1,6)
    return num


def mark_on_board(board,mark,position):
    board[position] = board[position]+mark
    snake_board(board)

def clean(board,mark,position):
    board[position] = str(position)
    # snake_board(board)


print ("Welcome to the Snakes game..")

board = game_board()
player1_marker,player2_marker = player_marker()
turn = choose_first()
print (turn +" will go first")

last_pos = 0
last_pos1 = 0
final = 100
while True:

    if turn == 'Player 1':
        # snake_board(board)
        clean(board, player1_marker, last_pos)
        position = roll_dice()
        last_pos += position
        if last_pos <= final:
            mark_on_board(board,player1_marker,last_pos)

            if check_win(board,player1_marker) == True:
                print("Congratulations!  Player 1 has won the game ")
                exit()
            else:
                turn = 'Player 2'
        else:
            last_pos -= position
            turn = 'Player 2'

    else:
        # snake_board(board)
        clean(board,player2_marker,last_pos1)
        position1 = roll_dice()
        last_pos1 += position1
        if last_pos1 <= final:
            mark_on_board(board, player2_marker, last_pos1)
            # clean(board,player2_marker,last_pos1)
            if check_win(board, player2_marker) == True:
                print("Congratulations!  Player 2 has won the game ")
                exit()
            else:
                 turn = 'Player 1'
        else:
            last_pos1 -= position1
            turn = 'Player 1'
