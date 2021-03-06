#step  1, write a function that prints out a board
def display_board(board):
    print("This is the play board \n" )

    print(board[1] +  '|' + board[2] +  '|' + board[3])
    print('------')
    print(board[4] +  '|' + board[5] +  '|' + board[6])
    print('------')
    print(board[7] +  '|' + board[8]+  '|' + board[9])
    print('\n')


#created a test list for display_board
#filled board
# test_board = ['#','1','','3','4','5','6','7','8','9']
#empty board
# test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
# display_board(test_board)

#step2, write a function that can take a player input and assign their option
# X or O, use while loop to ask until you get the right answer

def player_input():
    mark = ''

    
    while not (mark == 'X' or mark == 'O'):
        
        mark = input('choose X or O:  ').upper()
        print('\n')

    
    if mark == 'X':
        return ('X', 'O')

    else:
        return ('O', 'X')
        


#Step 3, a function that takes input from user, it must be 1-9 and then assign a mark based on the number chosen
def place_marker(board, mark, position):
    board[position] = mark
    

# place_marker(test_board, 'X', 9)
# place_marker(test_board, 'X', 8)
# place_marker(test_board, 'X', 7)

# display_board(test_board)


#step 4, a function that takes in a board and choice (x or o ) and checks if that choice has won

def win_check(board,mark):
    #to check if there if a winner
    #check if rows have same choice
    return ((board[7] == board[8] == board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
# print(win_check(test_board,'X'))
# print('\n'*3)

#step 5, write a function that decides ramdonly which player goes first. using the random module
import random

def choose_first():
    # players = ["player 1", "player 2"]
    # first = print('You go first: ', random.choice(players))
    # return first
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
# random_player()

#step 6, write a function that returns a boolean indicating wheter a space on the board is freely available

def space_check(board, position):
    return board[position] == ' '

# print(space_check(test_board, 3))
# print('\n'*3)


# step 7, check if the board is full and return a boolean
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
# test_board = ['#','1','2','3','','5','6','7','8','9']

# print(full_board_check(test_board))
# print('\n'*3)


#step 8, write a function that asks a player's next position (from 1-9) and then uses the fucntion in step 6 to check empty space
#if so, return position for later use

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Pick your next position from 1-9   '))
        
    return position      

# print(player_choice(test_board))
# print('\n'*3)


#step 9, write a function that asks a player if they want to play again and returns a boolean True if they do
def replay():

    return input('Play again Y or N  ').lower().startswith('y')


# print(replay())

#step 10, put all function to work and make the game run using While loops
print('\n'*5)
print('Welcome to Tic Tac Toe!')
print('\n'*5)
while True:
    # #reset board
    myBoard = [' '] * 10
    player1_choice, player2_choice = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    print('\n')
    
    play_game = input('Are you ready to play, Y or N ?    ').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    #GAME PLAY
    while game_on:
        #player 1 turn
        if turn == "Player 1":
            #show the board
            display_board(myBoard)
            #choose a position
            position = player_choice(myBoard)
            #place marker on the position
            place_marker(myBoard, player1_choice, position)

            #check if player won
            if win_check(myBoard, player1_choice):
                display_board(myBoard) 
                print('Congratulations! You have won the game!')
                print("\n")
                game_on = False
            else:
                #check game is a tie
                if full_board_check(myBoard):
                    display_board(myBoard)
                    print('The game is a draw')
                    break
                else:
                    #next players turn 
                    turn = 'Player 2'
        else:
            #player 2 turn
            display_board(myBoard)
            position = player_choice(myBoard)
            place_marker(myBoard, player2_choice, position)

            if win_check(myBoard, player2_choice):
                display_board(myBoard)
                game_on = False
            else:
                if full_board_check(myBoard):
                    display_board(myBoard)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 1'
        
    if not replay():
        print('\n')
        print('Thanks for playing')
        print('\n')
        break

