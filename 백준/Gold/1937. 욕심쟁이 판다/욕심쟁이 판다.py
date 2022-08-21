from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def find_max_path(r, c):
    if count_board[r][c] == -1:
        num = board[r][c]
        count = 0
        
        for r_dir, c_dir in dirs:
            next_r = r+r_dir
            next_c = c+c_dir
            if 0 <= next_r < n and 0 <= next_c < n and board[next_r][next_c] > num:
                temp = find_max_path(next_r, next_c)
                if temp > count:
                    count = temp
        count_board[r][c] = count+1
        
    return count_board[r][c]

n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
count_board = [[-1 for __ in range(n)] for _ in range(n)]

result = 0
for i in range(n):
    for j in range(n):
        temp = find_max_path(i, j)
        if temp > result:
            result = temp
print(result)