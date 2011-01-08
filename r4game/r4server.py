# a connect four "server" will import and call the players

import sys

def makeBoard(x, y):
    board = []
    for n in range(y):
    	board.append([])
        for m in range(x):
            board[-1].append(0)
    return board

def printBoard(board):
    for n in range(len(board)):
    	row = board[len(board) - n - 1]
        for point in row:
            if point == 0:
            	char = '_'
            elif point == 1:
                char = 'X'
            elif point == 2:
                char = 'O'
            else:
            	char = '?'
            print char + ' ',
        print

def makeMove(move, player, board):
    y = findMinRow(move, board)
    board[y][move] = player

def setLoc(x, y, player, board):
    board[y][x] = player

# this method not used...
def findWinnerBad(board):
    # check rows
    for row in board:
    	x = 0
    	team = 0
    	repeat = 0
        while x < len(row):
            if row[x] != team:
            	team = row[x]
            	repeat = 1
            elif row[x] != 0:
                reapeat += 1
            if repeat >= 4:
            	return team
    # check columns
    for col in range(len(board)):
    	y = 0
    	team = 0
    	repeat = 0
        while y < len(board):
            if board[y][col] != team:
            	team = board[y][col]
            	repeat = 1
            elif board[y][col] != 0:
                repeat += 1
            if repeat >= 4:
            	return team
    # check forward diagonals
    for diag in range(len(board)*2 - 1):
    	pass

def moveIsValid(x, board):
    return isValid(x, findMinRow(x, board), board)

def isValid(x, y, board):
    return (x >= 0 and y >= 0 and y < len(board) and x < len(board[0]))

def findLength(x, y, board):
    team = board[y][x]
    if team == 0:
    	return 0
    dir_list = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
    max_len = 1
    for dir in dir_list:
    	yy = y
    	xx = x
        len = 0
        while isValid(xx, yy, board) and board[yy][xx] == team:
            yy += dir[1]
            xx += dir[0]
            len += 1
        if len > max_len:
            max_len = len
    return max_len

def findWinner(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if findLength(x, y, board) >= 4:
            	return board[y][x]
    return 0

def isFull(board):
    for row in board:
        for point in row:
            if point == 0:
            	return False
    return True

def findMinRow(x, board):
    y = 0
    while y < len(board) and board[y][x] != 0:
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
    winner = 0
    turn = 0
    while winner == 0:
        if isFull(board):
            break
        printBoard(board)
        player = turn%2 + 1
        if player == 1:
            move = player_one.move(player, board)
        else:
            move = player_two.move(player, board)
        if not moveIsValid(move, board):
            print "player %d forfeits" % player
            winner = player%2 + 1
        else:
            print "player %d moves to %i" % (player, move)
            makeMove(move, player, board)
            winner = findWinner(board)
        turn += 1
    printBoard(board)
    if winner:
    	print "player %d wins" % (winner)
    else:
    	print "tie"

if __name__ == '__main__':
    main()

