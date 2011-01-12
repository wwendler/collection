# r42server.py, a modification of r4server, different board format
# a connect four "server" will import and call the players

import sys

def makeBoard(x, y):
    board = bytearray()
    for n in range(y):
        for m in range(x):
            board.append(0)
    return board

def printBoard(cols, board):
    for n in range(len(board)):
    	x = n%cols
    	y = len(board)/cols - n/cols - 1
    	point = board[y*cols + x]
        if point == 0:
            char = '_'
        elif point == 1:
            char = 'X'
        elif point == 2:
            char = 'O'
        else:
            char = '?'
        print char + ' ',
        if (n + 1)%cols == 0:
            print

def makeMove(move, player, cols, board):
    y = findMinRow(move, cols, board)
    board[y* cols + move] = player

def setLoc(x, y, player, cols, board):
    board[y*cols + x] = player

def moveIsValid(x, cols, board):
    return isValid(x, findMinRow(x, cols, board), cols, board)

def isValid(x, y, cols, board):
    return (x >= 0 and y >= 0 and y*cols < len(board) and x < cols)

def findLength(x, y, cols, board):
    team = board[y*cols + x]
    if team == 0:
    	return 0
    dir_list = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
    max_len = 1
    for dir in dir_list:
    	yy = y
    	xx = x
        len = 0
        while isValid(xx, yy, cols, board) and board[yy*cols + xx] == team:
            yy += dir[1]
            xx += dir[0]
            len += 1
        if len > max_len:
            max_len = len
    return max_len

def findWinner(cols, board):
    for n in range(len(board)):
    	x = n%cols
    	y = n/cols
        if findLength(x, y, cols, board) >= 4:
            return board[n]
    return 0

def isFull(cols, board):
    for point in board:
    	if point == 0:
            return False
    return True

def findMinRow(x, cols, board):
    y = 0
    while y*cols < len(board) and board[y*cols + x] != 0:
    	y += 1
    return y

def main():
    xsize = 7
    ysize = 6
    player_one_name = sys.argv[1].split('.')[0]
    player_two_name = sys.argv[2].split('.')[0]
    player_one = __import__(player_one_name)
    player_two = __import__(player_two_name)
    board = makeBoard(xsize, ysize)
    #print str(board)
    winner = 0
    turn = 0
    while winner == 0:
        if isFull(xsize, board):
            break
        printBoard(xsize, board)
        player = turn%2 + 1
        if player == 1:
            move = player_one.move(player, xsize, board)
        else:
            move = player_two.move(player, xsize, board)
        if not moveIsValid(move, xsize, board):
            print "player %d forfeits" % player
            winner = player%2 + 1
        else:
            print "player %d moves to %i" % (player, move)
            makeMove(move, player, xsize, board)
            winner = findWinner(xsize, board)
        turn += 1
    printBoard(xsize, board)
    if winner:
    	print "player %d wins" % (winner)
    else:
    	print "tie"

if __name__ == '__main__':
    main()

