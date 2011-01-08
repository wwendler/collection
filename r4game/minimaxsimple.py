# minimaxsimple.py
# An ai using minimax

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

def minimax(player, board, recur):
    opp = opponent(player)
    winner = r4.findWinner(board)
    xlen = len(board[0])
    ylen = len(board)
    if winner == player:
    	return eval_max, -1, 0
    elif winner == opp:
    	return eval_min, -1, 0
    if recur == 0:
    	return eval(player, board), -1, 0
    min_score = eval_max
    min_time = recur
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
        score, m, time = minimax(opp, board, recur - 1)
        r4.setLoc(x, y, 0, board)
        if (score < min_score or score == min_score and time < min_time):
            min_score = score
            best_move = x
            min_time = time
    # if there are no valid moves
    if len(valid_moves) == 0:
    	min_score = 0
    # if you are going to lose...
    elif min_score == eval_max:
        # this is a random move, because moves was shuffled
        best_move = valid_moves[0]
    return -min_score, best_move, min_time + 1

def move(player, board):
    num_recur = 4
    score, best_move, min_time = minimax(player, board, num_recur)
    if score == eval_min:
        print "expected result: my loss in %i moves" % (min_time)
    elif score == eval_max:
        print "you are doomed in %i moves" % (min_time)
    else:
        print "expected score: %i, num_recur: %i, best move: %i" % (score,
                num_recur, best_move)
    return best_move

