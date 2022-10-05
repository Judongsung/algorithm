from sys import stdin

NOT_CHECKED = -1
DIRS = [(0, 1), (1, 0)]

def count_path(r=0, c=0):
    if memo[r][c] == NOT_CHECKED:
        memo[r][c] = 0
        for r_dir, c_dir in DIRS:
            next_r = r+r_dir*board[r][c]
            next_c = c+c_dir*board[r][c]
            if 0 <= next_r < n and 0 <= next_c < n:
                memo[r][c] += count_path(next_r, next_c)
    return memo[r][c]

n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
memo = [[NOT_CHECKED for __ in range(n)] for _ in range(n)]
memo[n-1][n-1] = 1
print(count_path())