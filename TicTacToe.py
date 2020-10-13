#step  1, write a function that prints out a board
def display_board(board):
    print(board[1] +  '|' + board[2] +  '|' + board[3])
    print('------')
    print(board[4] +  '|' + board[5] +  '|' + board[6])
    print('------')
    print(board[7] +  '|' + board[8]+  '|' + board[9])
    print('\n')


#created a test list for display_board
#filled board
test_board = ['#','1','2','3','4','5','6','7','8','9']
#empty board
# test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
print("This is the play board \n" )
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
    
    #print players choices
    print('Player 1 :', player1,   '  Player 2 :', player2) 
    
    
    return player1, player2

player_input() 


#Step 3, a function that takes input from user, it must be 1-9 and then assign a mark based on the number chosen
def place_marker(board, choice, position):
    display_board(board)
    print('\n'*3)
    # play_board = []

    position = int(input('Player 1, you start, pick a number between 1 and 9'))
    
    test_board[position] = player_input() 

    return display_board(test_board)
place_marker(test_board, 'X', '9')