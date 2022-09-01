from sys import stdin

dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

def dfs(start_r, start_c):
    cur_r = start_r
    cur_c = start_c
    passed_loc = set()
    
    while not visited[cur_r][cur_c]:
        visited[cur_r][cur_c] = True
        passed_loc.add((cur_r, cur_c))
        r_dir, c_dir = dirs[board[cur_r][cur_c]]
        cur_r += r_dir
        cur_c += c_dir
        
    if (cur_r, cur_c) in passed_loc:
        result = 1
    else:
        result = 0
        
    return result

n, m = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(n)]
visited = [[False for __ in range(m)] for _ in range(n)]
count = 0

for r in range(n):
    for c in range(m):
        if not visited[r][c]:
            count += dfs(r, c)
            
print(count)