from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

def check_island(w, h, board, visited, r, c):
    if visited[r][c]:
        return
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    visited[r][c] = True
    
    for r_dir, c_dir in dirs:
        if 0 <= r+r_dir < h and 0 <= c+c_dir < w and board[r][c] == '1':
            check_island(w, h, board, visited, r+r_dir, c+c_dir)

def solution(w, h, board):
    visited = [[False]*w for _ in range(h)]
    island_count = 0
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == '1' and not visited[i][j]:
                check_island(w, h, board, visited, i, j)
                island_count += 1
    
    return island_count

while True:
    w, h = map(int, stdin.readline().split())
    if w == 0 and h == 0:
        break
        
    board = [stdin.readline().split() for _ in range(h)]
    result = solution(w, h, board)
    print(result)