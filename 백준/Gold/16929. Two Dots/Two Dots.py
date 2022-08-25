from sys import stdin
from collections import deque

dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def check_cycle(r, c):
    ch = board[r][c]
    queue = deque([(r, c, 0)])
    connected = {}
    
    while queue:
        cur_r, cur_c, count = queue.pop()
        if (cur_r, cur_c) in connected:
            if count-connected[(cur_r, cur_c)] >= 4:
                return True
            else:
                continue
        connected[(cur_r, cur_c)] = count
        next_count = count+1
        visited[r][c] = True
        
        for r_dir, c_dir in dirs:
            next_r = cur_r+r_dir
            next_c = cur_c+c_dir
            
            if 0 <= next_r < row and 0 <= next_c < col and board[next_r][next_c] == ch:
                queue.append((next_r, next_c, next_count))
    return False

row, col = map(int, stdin.readline().split())
board = [list(stdin.readline()) for _ in range(row)]
visited = [[False for __ in range(col)] for _ in range(row)]

result = 'No'
flag = True
for r in range(row):
    for c in range(col):
        if not visited[r][c]:
            if check_cycle(r, c):
                result = 'Yes'
                flag = False
                break
    if not flag:
        break
        
print(result)