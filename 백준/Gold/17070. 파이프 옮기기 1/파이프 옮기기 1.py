from sys import stdin

EMPTY = '0'
WALL = '1'
RIGHT = 0
DOWN = 1
RIGHT_DOWN = 2

n = int(stdin.readline())
board = [stdin.readline().split() for _ in range(n)]
memo = [[[0]*3 for _ in range(n)] for __ in range(n)]

memo[0][1][RIGHT] = 1
for c in range(1, n):
    if board[0][c] == WALL:
        break
    memo[0][c][RIGHT] = 1
    
for r in range(1, n):
    for c in range(1, n):
        if board[r][c] == EMPTY:
            memo[r][c][RIGHT] = memo[r][c-1][RIGHT]+memo[r][c-1][RIGHT_DOWN]
            memo[r][c][DOWN] = memo[r-1][c][DOWN]+memo[r-1][c][RIGHT_DOWN]
            
            if board[r-1][c] == EMPTY and board[r][c-1] == EMPTY:
                memo[r][c][RIGHT_DOWN] = memo[r-1][c-1][RIGHT]+memo[r-1][c-1][DOWN]+memo[r-1][c-1][RIGHT_DOWN]

result = sum(memo[n-1][n-1])
print(result)