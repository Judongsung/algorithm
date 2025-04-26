from sys import stdin

def dfs(board, row, col):
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    max_count = 1
    queue = set()
    queue.add((0, 0, board[0][0]))
    
    while queue:
        r, c, route = queue.pop()
        
        flag = False
        for r_dir, c_dir in dirs:
            next_r = r+r_dir
            next_c = c+c_dir
            if 0 <= next_r < row and 0 <= next_c < col and board[next_r][next_c] not in route:
                queue.add((next_r, next_c, route+board[next_r][next_c]))
                flag = True
        
        if not flag:
            max_count = max(len(route), max_count)
            if max_count == 26:
                break
    
    return max_count


row, col = map(int, stdin.readline().split())
board = [stdin.readline() for _ in range(row)]
result = dfs(board, row, col)
print(result)