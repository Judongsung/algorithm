from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

EMPTY = '.'
USING = 'x'
directions = [(-1, 1), (0, 1), (1, 1)]

def find_path(cur_r, cur_c, goal, board):
    board[cur_r][cur_c] = USING
    if cur_c == goal:
        return True
    
    for r_dir, c_dir in directions:
        next_r = cur_r+r_dir
        next_c = cur_c+c_dir
        if 0 <= next_r < r and 0 <= next_c < c and board[next_r][next_c] != USING and find_path(next_r, next_c, goal, board):
            return True
    
    return False

r, c = map(int, stdin.readline().split())
board = [list(stdin.readline()) for _ in range(r)]
count = 0
goal = c-2

for i in range(r):
    if board[i][1] == USING:
        continue
    result = find_path(i, 1, goal, board)
    if result == True:
        count += 1
print(count)