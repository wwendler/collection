# abminimax.py
# An ai using minimax and alpha beta pruning

import r4server as r4
import random

def opponent(player):
    return player%2+1

eval_max = 9999
eval_min = -9999

def eval(player, board):
    count = 0
    opp = opponent(player)
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == player:
            	count += r4.findLength(x, y, board)
            elif board[y][x] == opp:
            	count -= r4.findLength(x, y, board)
    return count

def eval2(player, board):
    count = 0
    opp = opponent(player)
    for x in range(len(board[0])):
    	y = r4.findMinRow(x, board)
        if not r4.isValid(x, y, board):
            continue
    	r4.setLoc(x, y, player, board)
    	length = r4.findLength(x, y, board)
        if length >= 4:
            count += 1
        elif r4.isValid(x, y+1, board):
            r4.setLoc(x, y+1, opp, board)
            length = r4.findLength(x, y+1, board)
            if length >= 4:
            	count -= 1
            r4.setLoc(x, y+1, 0, board)
        r4.setLoc(x, y, 0, board)
    return count

# player is always the min player...
def abminimax(player, board, recur, alpha, beta):
    opp = opponent(player)
    winner = r4.findWinner(board)
    xlen = len(board[0])
    ylen = len(board)
    if winner == player:
    	return eval_max, -1
    elif winner == opp:
    	return eval_min, -1
    if recur == 0:
    	return eval2(player, board), -1
    best_move = -1
    valid_moves = []
    moves = range(xlen)
    random.shuffle(moves)
    for x in moves:
    	y = r4.findMinRow(x, board)
        if r4.isValid(x, y, board):
            valid_moves.append(x)
        else:
            continue
        r4.setLoc(x, y, player, board)
        score, bluh = abminimax(opp, board, recur - 1,
                -beta, -alpha)
        r4.setLoc(x, y, 0, board)
        if score < beta:
            beta = score
            best_move = x
        if beta <= alpha:
            #print "ab pruning, returning %s" % str((beta, recur, best_move))
            return -beta, best_move
    # if there are no valid moves
    if len(valid_moves) == 0:
    	beta = min(beta, 0)
    # if you are going to lose...
    elif beta == eval_max:
        # this is a random move, because moves was shuffled
        best_move = valid_moves[0]
    return -beta, best_move

def move(player, board):
    num_recur = 6
    score, best_move = abminimax(player, board,
            num_recur, eval_min, eval_max)
    if score == eval_min:
        print "expected result: my loss. moving to %i" % best_move
    elif score == eval_max:
        print "you are doomed. moving to %i" % best_move
    else:
        print "expected score: %i, num_recur: %i, best move: %i" % (score,
                num_recur, best_move)
    return best_move

