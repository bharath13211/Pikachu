#
# pikachu.py : Play the game of Pikachu
#
# PLEASE PUT YOUR NAMES AND USER IDS HERE!
#
# Based on skeleton code by D. Crandall, March 2021
#
import sys
import time
import copy
import math
from queue import PriorityQueue

def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))

def conv_to_2d(board):
    N = int(math.sqrt(len(board)))
    b_2d = []
    lis = []
    for i in range(0, len(board)):
        lis.append(board[i])
        if len(lis) == N:
            b_2d.append(lis)
            lis = []
    return b_2d


def move_left_w_jump(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N and c >= 2 and temp_board[r][c] == 'w':
        if (temp_board[r][c - 1] == 'b' or temp_board[r][c - 1] == 'B') and temp_board[r][c - 2] == '.':
            temp_board[r][c - 2] = player
            temp_board[r][c - 1] = '.'
            temp_board[r][c] = '.'
    return temp_board

def move_left_w_1(board,player,N,r,c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N and c >= 1 and temp_board[r][c] == 'w':
        if temp_board[r][c - 1] == '.':
            temp_board[r][c - 1] = player
            temp_board[r][c] = '.'
    return temp_board

def move_right_w(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N - 2 and c >= 0 and temp_board[r][c] == 'w':
        if (temp_board[r][c + 1] == 'b' or temp_board[r][c + 1] == 'B') and temp_board[r][c + 2] == '.':
            temp_board[r][c + 2] = player
            temp_board[r][c + 1] = '.'
            temp_board[r][c] = '.'
    return temp_board

def move_right_w_1(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N - 1 and c >= 0 and temp_board[r][c] == 'w':
        if temp_board[r][c + 1] == '.':
            temp_board[r][c + 1] = player
            temp_board[r][c] = '.'
    return temp_board

def move_right_b_jump(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N and c >= 2 and board[r][c] == 'b':
        if (temp_board[r][c - 1] == 'w' or temp_board[r][c - 1] == 'W') and temp_board[r][c - 2] == '.':
            temp_board[r][c - 2] = player
            temp_board[r][c - 1] = '.'
            temp_board[r][c] = '.'
    return temp_board

def move_right_b_1(board,player,N,r,c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N and c >= 1 and temp_board[r][c] == 'b':
        if temp_board[r][c - 1] == '.':
            temp_board[r][c - 1] = player
            temp_board[r][c] = '.'
    return temp_board

def move_left_b(board,player,N,r,c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N - 2 and c >= 0 and temp_board[r][c] == 'b':
        if (temp_board[r][c + 1] == 'w' or temp_board[r][c + 1] == 'W') and temp_board[r][c + 2] == '.':
            temp_board[r][c + 2] = player
            temp_board[r][c + 1] = '.'
            temp_board[r][c] = '.'
    return temp_board

def move_left_b_1(board,player,N,r,c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N - 1 and c >= 0 and temp_board[r][c] == 'b':
        if temp_board[r][c + 1] == '.':
            temp_board[r][c + 1] = player
            temp_board[r][c] = '.'
    return temp_board

def move_down_w_jump(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N-2 and r >= 0 and c < N and c >= 0 and temp_board[r][c] == 'w':
        if (temp_board[r + 1][c] == 'b' or temp_board[r + 1][c] == 'B') and temp_board[r + 2][c] == '.':
            if r + 2 == N - 1:
                temp_board[r + 2][c] = 'W'
                temp_board[r + 1][c] = '.'
                temp_board[r][c] = '.'
            else:
                temp_board[r + 2][c] = player
                temp_board[r + 1][c] = '.'
                temp_board[r][c] = '.'
    return temp_board

def move_down_w_1(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N - 1 and r >= 0 and c < N and c >= 0 and temp_board[r][c] == 'w':
        if temp_board[r + 1][c] == '.':
            if r + 1 == N - 1:
                temp_board[r + 1][c] = 'W'
                temp_board[r][c] = '.'
            else:
                temp_board[r + 1][c] = player
                temp_board[r][c] = '.'
    return temp_board

def move_up_b_jump(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N  and r >= 2 and c < N and c >= 0 and temp_board[r][c] == 'b':
        if (temp_board[r - 1][c] == 'w' or temp_board[r - 1][c] == 'W') and temp_board[r - 2][c] == '.':
            if r - 2 == 0:
                temp_board[r - 2][c] = 'B'
                temp_board[r - 1][c] = '.'
                temp_board[r][c] = '.'
            else:
                temp_board[r - 2][c] = player
                temp_board[r - 1][c] = '.'
                temp_board[r][c] = '.'
    return temp_board

def move_up_b_1(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 1 and c < N and c >= 0 and temp_board[r][c] == 'b':
        if temp_board[r - 1][c] == '.':
            if r - 1 == 0:
                temp_board[r - 1][c] = 'B'
                temp_board[r][c] = '.'
            else:
                temp_board[r - 1][c] = player
                temp_board[r][c] = '.'
    return temp_board

def move_W_left(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N and c >= 2 and temp_board[r][c] == 'W':
        for j in range(1, c):
            if (temp_board[r][j] == 'b' or temp_board[r][j] == 'B') and temp_board[r][j - 1] == '.':
                list = []
                for k in range(j, c):
                    if temp_board[r][k] == 'w' or temp_board[r][k] == 'W':
                        list.append('N')
                    elif temp_board[r][k] == '.':
                        list.append('Y')
                if 'N' not in list:
                    temp_board[r][j - 1] = 'W'
                    temp_board[r][j] = '.'
                    temp_board[r][c] = '.'
    return temp_board

def move_W_left_1(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N and c >= 1 and temp_board[r][c] == 'W':
        if temp_board[r][c - 1] == '.':
            temp_board[r][c - 1] = 'W'
            temp_board[r][c] = '.'
    return temp_board

def move_W_right(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N - 2 and c >= 0 and temp_board[r][c] == 'W':
        for j in range(c + 1, N-1):
            if (temp_board[r][j] == 'b' or temp_board[r][j] == 'B') and temp_board[r][j + 1] == '.':
                list = []
                for k in range(c + 1, j):
                    if temp_board[r][k] == 'w' or temp_board[r][k] == 'W':
                        list.append('N')
                    elif temp_board[r][k] == '.':
                        list.append('Y')
                if 'N' not in list:
                    temp_board[r][j + 1] = 'W'
                    temp_board[r][j] = '.'
                    temp_board[r][c] = '.'
    return temp_board

def move_W_right_1(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N - 1 and c >= 0 and temp_board[r][c] == 'W':
        if temp_board[r][c + 1] == '.':
            temp_board[r][c + 1] = 'W'
            temp_board[r][c] = '.'
    return temp_board

def move_W_down(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N - 2 and r >= 0 and c < N and c >= 0 and temp_board[r][c] == 'W':
        for j in range(r + 1, N - 1):
            if (temp_board[j][c] == 'b' or temp_board[j][c] == 'B') and temp_board[j + 1][c] == '.':
                list = []
                for k in range(r + 1, j):
                    if temp_board[k][c] == 'w' or temp_board[k][c] == 'W':
                        list.append('N')
                    elif temp_board[k][c] == '.':
                        list.append('Y')
                if 'N' not in list:
                    temp_board[j + 1][c] = 'W'
                    temp_board[j][c] = '.'
                    temp_board[r][c] = '.'
    return temp_board

def move_W_down_1(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N - 1 and r >= 0 and c < N and c >= 0 and temp_board[r][c] == 'W':
        if temp_board[r + 1][c] == '.':
            temp_board[r + 1][c] = 'W'
            temp_board[r][c] = '.'
    return temp_board

def move_W_up(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N  and r >= 2 and c < N and c >= 0 and temp_board[r][c] == 'W':
        for j in range(1, r):
            if (temp_board[j][c] == 'b' or temp_board[j][c] == 'B') and temp_board[j - 1][c] == '.':
                list = []
                for k in range(j, r):
                    if temp_board[k][c] == 'w' or temp_board[k][c] == 'W':
                        list.append('N')
                    elif temp_board[k][c] == '.':
                        list.append('Y')
                if 'N' not in list:
                    temp_board[j - 1][c] = 'W'
                    temp_board[j][c] = '.'
                    temp_board[r][c] = '.'
    return temp_board

def move_W_up_1(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 1 and c < N and c >= 0 and temp_board[r][c] == 'W':
        if temp_board[r - 1][c] == '.':
            temp_board[r - 1][c] = 'W'
            temp_board[r][c] = '.'
    return temp_board

def move_B_right(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N and c >= 2 and temp_board[r][c] == 'B':
        for j in range(1, c):
            if (temp_board[r][j] == 'w' or temp_board[r][j] == 'W') and temp_board[r][j - 1] == '.':
                list = []
                for k in range(j, c):
                    if temp_board[r][k] == 'b' or temp_board[r][k] == 'B':
                        list.append('N')
                    elif temp_board[r][k] == '.':
                        list.append('Y')
                if 'N' not in list:
                    temp_board[r][j - 1] = 'B'
                    temp_board[r][j] = '.'
                    temp_board[r][c] = '.'
    return temp_board

def move_B_right_1(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N and c >= 1 and temp_board[r][c] == 'B':
        if temp_board[r][c - 1] == '.':
            temp_board[r][c - 1] = 'B'
            temp_board[r][c] = '.'
    return temp_board

def move_B_left(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N - 2 and c >= 0 and temp_board[r][c] == 'B':
        for j in range(c + 1, N-1):
            if (temp_board[r][j] == 'w' or temp_board[r][j] == 'W') and temp_board[r][j + 1] == '.':
                list = []
                for k in range(c + 1, j):
                    if temp_board[r][k] == 'b' or temp_board[r][k] == 'B':
                        list.append('N')
                    elif temp_board[r][k] == '.':
                        list.append('Y')
                if 'N' not in list:
                    temp_board[r][j + 1] = 'B'
                    temp_board[r][j] = '.'
                    temp_board[r][c] = '.'
    return temp_board

def move_B_left_1(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 0 and c < N - 1 and c >= 0 and temp_board[r][c] == 'B':
        if temp_board[r][c + 1] == '.':
            temp_board[r][c + 1] = 'B'
            temp_board[r][c] = '.'
    return temp_board

def move_B_up(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N - 2 and r >= 0 and c < N and c >= 0 and temp_board[r][c] == 'B':
        for j in range(r + 1, N - 1):
            if (temp_board[j][c] == 'w' or temp_board[j][c] == 'W') and temp_board[j + 1][c] == '.':
                list = []
                for k in range(r + 1, j):
                    if temp_board[k][c] == 'b' or temp_board[k][c] == 'B':
                        list.append('N')
                    elif temp_board[k][c] == '.':
                        list.append('Y')
                if 'N' not in list:
                    temp_board[j + 1][c] = 'B'
                    temp_board[j][c] = '.'
                    temp_board[r][c] = '.'
    return temp_board

def move_B_up_1(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N - 1 and r >= 0 and c < N and c >= 0 and temp_board[r][c] == 'B':
        if temp_board[r + 1][c] == '.':
            temp_board[r + 1][c] = 'B'
            temp_board[r][c] = '.'
    return temp_board

def move_B_down(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N  and r >= 2 and c < N and c >= 0 and temp_board[r][c] == 'B':
        for j in range(1, r):
            if (temp_board[j][c] == 'w' or temp_board[j][c] == 'W') and temp_board[j - 1][c] == '.':
                list = []
                for k in range(j, r):
                    if temp_board[k][c] == 'b' or temp_board[k][c] == 'B':
                        list.append('N')
                    elif temp_board[k][c] == '.':
                        list.append('Y')
                if 'N' not in list:
                    temp_board[j - 1][c] = 'B'
                    temp_board[j][c] = '.'
                    temp_board[r][c] = '.'
    return temp_board

def move_B_down_1(board, player, N, r, c):
    temp_board = copy.deepcopy(board)
    if r < N and r >= 1 and c < N and c >= 0 and temp_board[r][c] == 'B':
        if temp_board[r - 1][c] == '.':
            temp_board[r - 1][c] = 'B'
            temp_board[r][c] = '.'
    return temp_board


def successors(board,player,N):
    board1 = copy.deepcopy(board)
    board1 = conv_to_2d(board1)
    list_successors_w = []
    list_successors_b = []
    for r in range(0, N):
        for c in range(0, N):
            if move_left_w_jump(board, 'w', N, r, c) != board1:
                list_successors_w.append(move_left_w_jump(board, 'w', N, r, c))
            if move_left_w_1(board, 'w', N, r, c) != board1:
                list_successors_w.append(move_left_w_1(board, 'w', N, r, c))
            if move_right_w(board, 'w', N, r, c) != board1:
                list_successors_w.append(move_right_w(board, 'w', N, r, c))
            if move_right_w_1(board, 'w', N, r, c) != board1:
                list_successors_w.append(move_right_w_1(board, 'w', N, r, c))
            if move_down_w_jump(board, 'w', N, r, c) != board1:
                list_successors_w.append(move_down_w_jump(board, 'w', N, r, c))
            if move_down_w_1(board, player, N, r, c) != board1:
                list_successors_w.append(move_down_w_1(board, 'w', N, r, c))
            if move_W_left(board, 'W', N, r, c) != board1:
                list_successors_w.append(move_W_left(board, 'W', N, r, c))
            if move_W_left_1(board, 'W', N, r, c) != board1:
                list_successors_w.append(move_W_left_1(board, 'W', N, r, c))
            if move_W_right(board, 'W', N, r, c) != board1:
                list_successors_w.append(move_W_right(board, 'W', N, r, c))
            if move_W_right_1(board, 'W', N, r, c) != board1:
                list_successors_w.append(move_W_right_1(board, 'W', N, r, c))
            if move_W_down(board, 'W', N, r, c) != board1:
                list_successors_w.append(move_W_down(board, 'W', N, r, c))
            if move_W_down_1(board, 'W', N, r, c) != board1:
                list_successors_w.append(move_W_down_1(board, 'W', N, r, c))
            if move_W_up(board, 'W', N, r, c) != board1:
                list_successors_w.append(move_W_up(board, 'W', N, r, c))
            if move_W_up_1(board, 'W', N, r, c) != board1:
                list_successors_w.append(move_W_up_1(board, 'W', N, r, c))
            if move_right_b_jump(board, 'b', N, r, c) != board1:
                list_successors_b.append(move_right_b_jump(board, 'b', N, r, c))
            if move_right_b_1(board, 'b', N, r, c) != board1:
                list_successors_b.append(move_right_b_jump(board, 'b', N, r, c))
            if move_left_b(board, 'b', N, r, c) != board1:
                list_successors_b.append(move_left_b(board, 'b', N, r, c))
            if move_left_b_1(board, 'b', N, r, c) != board1:
                list_successors_b.append(move_left_b_1(board, 'b', N, r, c))
            if move_up_b_jump(board, 'b', N, r, c) != board1:
                list_successors_b.append(move_up_b_jump(board, 'b', N, r, c))
            if move_up_b_1(board, 'b', N, r, c) != board1:
                list_successors_b.append(move_up_b_1(board, 'b', N, r, c))
            if move_B_right(board, 'B', N, r, c) != board1:
                list_successors_b.append(move_B_right(board, 'B', N, r, c))
            if move_B_right_1(board, 'B', N, r, c) != board1:
                list_successors_b.append(move_B_right_1(board, 'B', N, r, c))
            if move_B_left(board, 'B', N, r, c) != board1:
                list_successors_b.append(move_B_left(board, 'B', N, r, c))
            if move_B_left_1(board, 'B', N, r, c) != board1:
                list_successors_b.append(move_B_left_1(board, 'B', N, r, c))
            if move_B_up(board, 'B', N, r, c) != board1:
                list_successors_b.append(move_B_up(board, 'B', N, r, c))
            if move_B_up_1(board, 'B', N, r, c) != board1:
                list_successors_b.append(move_B_up_1(board, 'B', N, r, c))
            if move_B_down(board, 'B', N, r, c) != board1:
                list_successors_b.append(move_B_down(board, 'B', N, r, c))
            if move_B_down_1(board, 'B', N, r, c) != board1:
                list_successors_b.append(move_B_down_1(board, 'B', N, r, c))
    if player == 'w':
        return list_successors_w
    else:
        return list_successors_b

def evaluatefunc(board,N,player):
    count_W = 0
    count_w = 0
    count_b = 0
    count_B = 0
    if player=='w':
        for i in board:
            if i == 'W':
                count_W += 1
            elif i == 'w':
                count_w += 1
            elif i == 'B':
                count_B += 1
            elif i == 'b':
                count_b += 1
        return ((2 * count_W) + (count_w) - (2 * count_B) - (count_b))

    if player=='b':
        for i in board:
            if i == 'W':
                count_W += 1
            elif i == 'w':
                count_w += 1
            elif i == 'B':
                count_B += 1
            elif i == 'b':
                count_b += 1
        return ((2 * count_B) + (count_b) - (2 * count_W) - (count_w))


def checkfinalstate(successor,N):
    b=0
    w=0
    for i in range(N):
        for j in range(N):
            if(successor[i][j]=="b" or successor[i][j]=="B" ):
                b+=1
            if(successor[i][j]=="w" or successor[i][j]=="W"):
                w+=1
    if(b==0 or w==0):
        return True
    else:
        return False


def min_v(successor, a, b, level, player, limit, N):
    level += 1
    if time.time() >= endtime - 1:
        sys.exit(0)
    if level == limit or checkfinalstate(successor,N):
        return evaluatefunc(successor, N, player)
    else:
        if (player=="w"):
            opponent="b"
        else:
            opponent="w"
        maxsuccessors = successors(successor, opponent,N)
        for i in maxsuccessors:
            b = min(b, max_v(i, a, b, level, player, limit,N))
            if a >= b:
                return b
        return b

def max_v(successor, a, b, level, player, limit,N):
    level += 1
    if time.time() >= endtime - 1:
        sys.exit(0)
    if level == limit or checkfinalstate(successor, N):
        return evaluatefunc(successor, N,player)
    else:
        minsuccessors = successors(successor, player,N)
        for i in minsuccessors:
            a = max(a, min_v(i, a, b, level, player, limit,N))
            if a >= b:
                return a
        return a

def min_max(board,player,N,level):
    succ=successors(board,player,N)
    fringe=PriorityQueue()
    betabydefault = 100000000
    alphabydefault = -10000000
    for minsucc in succ:
        fringe.put((min_v(minsucc, alphabydefault, betabydefault, 0, player, level, N) * -1, minsucc))
    a=fringe.get()
    return a[1]


def find_best_move(board, N, player, timelimit):
    boardList=[]
    i=0
    while i<N*N:
        li = []
        for j in range(N):
            li.append(board[i])
            i+=1
        boardList.append(li)
    global endtime
    endtime = time.time() + float(timelimit)
    depth=1
    while True:
        result= min_max(boardList, player, N,depth)
        str1 = ""
        for i in result:
            for j in i:
                str1+=j
        yield str1
        depth+=1

if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: pikachu.py N player board timelimit")
    (_, N, player, board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N*N or 0 in [c in "wb.WB" for c in board]:
        raise Exception("Bad board string.")
    boardList = []
    i = 0
    while i < N * N:
        li = []
        for j in range(N):
            li.append(board[i])
            i += 1
        boardList.append(li)
    #successors(boardList, 'b', 7)
    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    for new_board in find_best_move(board, N, player, timelimit):
        print(board_to_string(new_board,N))