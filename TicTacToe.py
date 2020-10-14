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
test_board = ['#','1','','3','4','5','6','7','8','9']
#empty board
# test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
print("This is the play board \n" )
display_board(test_board)

#step2, write a function that can take a player input and assign their option
# X or O, use while loop to ask until you get the right answer

def player_input():
    choice = ''

    
    while choice != 'X' and choice != 'O':
        
        choice = input('Player1, choose X or O:  ').upper()
        print('\n')
    player1 = choice
    
    if player1 == 'X':
        player2 = 'O'

    else:
        player2 = 'X'
    
    #print players choices
    print('Player 1 :', player1,   '  Player 2 :', player2) 
    
    
    return player1, player2
    print('\n' *2)

player_input() 


#Step 3, a function that takes input from user, it must be 1-9 and then assign a mark based on the number chosen
def place_marker(board, choice, position):
    board[position] = choice

place_marker(test_board, 'X', 9)
place_marker(test_board, 'X', 8)
place_marker(test_board, 'X', 7)

display_board(test_board)


#step 4, a function that takes in a board and choice (x or o ) and checks if that choice has won

def win_check(board,choice):
    #to check if there if a winner
    #check if rows have same choice
    if ((board[1]== board[2] == board[3] == choice) or
        (board[4]== board[5] == board[6] == choice) or 
        (board[7]== board[8] == board[9] == choice) or 
        
    #check if columns have same choice 
        (board[1]== board[4] == board[7] == choice) or 
        
        (board[2]== board[5] == board[8] == choice) or 
        
        (board[3]== board[7] == board[9] == choice) or
        
    #check if diagonals have same choice
        (board[1]== board[5] == board[9] == choice) or
        (board[3]== board[5] == board[7] == choice)):
        return "Congratulations, you won the game!"

    #no winner yet

    return "not a winner yet"
   
print(win_check(test_board,'X'))
print('\n'*3)

#step 5, write a function that decides ramdonly which player goes first. using the random module
import random

def random_player():
    players = ["player 1", "player 2"]
    first = print('You go first: ', random.choice(players))
    return first
random_player()

#step 6, write a function that returns a boolean indicating wheter a space on the board is freely available

def space_check(board, position):
    return board[position] == ''

print(space_check(test_board, 3))

# step 7, check if the board is full and return a boolean
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
test_board = ['#','1','2','3','4','5','6','7','8','9']

print(full_board_check(test_board))