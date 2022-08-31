from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def dfs(r, c):
    if memo[r][c] == -1:
        count = 0
        cur_height = board[r][c]
        
        for r_dir, c_dir in dirs:
            next_r = r+r_dir
            next_c = c+c_dir
            if 0 <= next_r < row and 0 <= next_c < col and board[next_r][next_c] < cur_height:
                count += dfs(next_r, next_c)
        memo[r][c] = count
    return memo[r][c]

row, col = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(row)]
memo = [[-1 for __ in range(col)] for _ in range(row)]
memo[row-1][col-1] = 1

result = dfs(0, 0)
print(result)