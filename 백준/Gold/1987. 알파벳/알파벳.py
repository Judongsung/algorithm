from sys import stdin

def dfs(board, row, col, visited=[False for _ in range(26)], cur_r=0, cur_c=0):
    cur_alpha = board[cur_r][cur_c]
    alpha_idx = ord(cur_alpha)-65
    if visited[alpha_idx]:
        return 0
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    cur_visited = visited.copy()
    cur_visited[alpha_idx] = True
    max_count = 0
    
    for r_dir, c_dir in dirs:
        next_r = cur_r+r_dir
        next_c = cur_c+c_dir
        if 0 <= next_r < row and 0 <= next_c < col:
            temp = dfs(board, row, col, cur_visited, next_r, next_c)
            max_count = max(temp, max_count)
    
    return max_count+1


row, col = map(int, stdin.readline().split())
board = [stdin.readline() for _ in range(row)]
result = dfs(board, row, col)
print(result)