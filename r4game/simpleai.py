# A simple AI... that will do stuff

import r4server as r4
import random

def move(player, board):
    xlen = len(board[0])
    ylen = len(board)
    moves = range(xlen)
    random.shuffle(moves)
    best_move = -1
    for m in moves:
    	y = r4.findMinRow(m, board)
    	if not r4.isValid(m, y, board):
    	    continue
    	r4.setLoc(m, y, player, board)
    	winner = r4.findWinner(board)
    	r4.setLoc(m, y, 0, board)
        if (winner == 0):
    	    best_move = m
        elif (winner == player):
            best_move = m
            break
    return best_move

