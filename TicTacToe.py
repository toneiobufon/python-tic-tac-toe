#step  1, write a function that prints out a board
def display_board(board):
    print(board[1] +  '|' + board[2] +  '|' + board[3])
    print('------')
    print(board[4] +  '|' + board[5] +  '|' + board[6])
    print('------')
    print(board[7] +  '|' + board[8]+  '|' + board[9])

#created a test list for display_board
#filled board
# test_board = ['#','X','O','X','O','X','O','X','O','X']
#empty board
test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(test_board)

#step2, write a function that can take a player input and assign their option
# X or O, use while loop to ask until you get the right answer

def player_input():
    choice = ''

    
    while choice != 'X' and choice != 'O':
        
        choice = input('Player1, choose X or O:  ')
        print('\n')
    player1 = choice
    
    if player1 == 'X':
        player2 = 'O'

    else:
        player2 = 'X'
    print('player 1 :', player1,   '  player 2 :', player2)
    
    
    return player1, player2

player_input() 