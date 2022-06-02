from sys import setrecursionlimit
from sys import stdin

setrecursionlimit(10**6)

def check_area(n, board, checked, h, r, c):
    checked[r][c] = True
    r_dirs = [-1, 0, 0, 1]
    c_dirs = [0, -1, 1, 0]
    
    for r_dir, c_dir in zip(r_dirs, c_dirs):
        nr = r+r_dir
        nc = c+c_dir
        if not (0 <= nr < n and 0 <= nc < n) or (board[nr][nc] <= h or checked[nr][nc]):
            continue
        check_area(n, board, checked, h, nr, nc)
    
    return

def count_areas(n, board, h):
    count = 0
    checked = [[False]*n for _ in range(n)]
    
    for r in range(n):
        for c in range(n):
            if board[r][c] <= h or checked[r][c]:
                continue
            check_area(n, board, checked, h, r, c)
            count += 1
    
    return count

def solution(n, board):
    h = 0
    max_h = max([max(row) for row in board])
    max_count = 0
    
    while h < max_h :
        count = count_areas(n, board, h)
        if count > max_count:
            max_count = count
        h += 1
    
    return max_count

n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
result = solution(n, board)
print(result)