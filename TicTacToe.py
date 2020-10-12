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