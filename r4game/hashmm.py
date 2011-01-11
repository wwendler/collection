# hashmm.py
# Adds hashing of scores to speed things up. meant to be used with r42 server

import r42server as r4
import random

def opponent(player):
    return player%2+1

eval_max = 9999
eval_min = -9999

def eval(player, cols, board):
    count = 0
    opp = opponent(player)
    for x in range(cols):
    	y = r4.findMinRow(x, cols, board)
        if y*cols > len(board):
            continue
    	board[y*cols + x] = player
    	length = r4.findLength(x, y, cols, board)
        if length >= 4:
            count += 1
        elif (y+1)*cols < len(board):
            board[(y+1)*cols + x] = opp
            length = r4.findLength(x, y+1, cols, board)
            if length >= 4:
            	count -= 1
            board[(y+1)*cols + x] = 0
        board[y*cols + x] = 0
    return count

def hashBoard(board):
    return hash(str(board))

# player is always the min player...
def abminimax(player, cols, board, recur, alpha, beta, dict):
    opp = opponent(player)
    winner = r4.findWinner(cols, board)
    xlen = cols
    ylen = len(board)/cols
    if winner == player:
    	return eval_max, -1
    elif winner == opp:
    	return eval_min, -1
    if recur == 0:
    	return eval(player, cols, board), -1
    b_hash = hashBoard(board)
    if b_hash in dict:
    	#print "skip!"
    	return dict[b_hash], -1
    best_move = -1
    valid_moves = []
    #moves = range(xlen)
    #random.shuffle(moves)
    for x in range(xlen):
    	y = r4.findMinRow(x, cols, board)
        if r4.isValid(x, y, cols, board):
            valid_moves.append(x)
        else:
            continue
        board[y*cols + x] = player
        score, bluh = abminimax(opp, cols, board, recur - 1,
                -beta, -alpha, dict)
        board[y*cols + x] = 0
        if score < beta:
            beta = score
            best_move = x
        if beta <= alpha:
            #print "ab pruning, returning %s" % str((beta, recur, best_move))
            dict[b_hash] = -beta
            return -beta, best_move
    # if there are no valid moves
    if len(valid_moves) == 0:
    	beta = min(beta, 0)
    # if you are going to lose...
    elif beta == eval_max:
        # this is a random move, because moves was shuffled
        best_move = valid_moves[0]
    dict[b_hash] = -beta
    return -beta, best_move

def move(player, cols, board):
    num_recur = 6
    score, best_move = abminimax(player, cols, board,
            num_recur, eval_min, eval_max, {})
    if score == eval_min:
        print "expected result: my loss. moving to %i" % best_move
    elif score == eval_max:
        print "you are doomed. moving to %i" % best_move
    else:
        print "expected score: %i, num_recur: %i, best move: %i" % (score,
                num_recur, best_move)
    return best_move

