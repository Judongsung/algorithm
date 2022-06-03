from sys import stdin

def get_empty_board(n, m):
    return [[0]*m for _ in range(n)]

def melt(r, c, board):
    r_dirs = [-1, 0, 0, 1]
    c_dirs = [0, -1, 1, 0]
    amount = board[r][c]
    
    for r_dir, c_dir in zip(r_dirs, c_dirs):
        sr = r+r_dir
        sc = c+c_dir
        if 0 <= sr < n and 0 <= sc < m and board[sr][sc] == 0:
            amount -= 1
    
    return max(amount, 0)

def is_multiple(n, m, board, glaciers):
    r_dirs = [-1, 0, 0, 1]
    c_dirs = [0, -1, 1, 0]
    visited = {}
    for r, c in glaciers:
        visited[(r, c)] = False
    queue = [glaciers[0]]
    visited[glaciers[0]] = True
    count = 0
    
    while queue:
        r, c = queue.pop(0)
        count += 1
        for r_dir, c_dir in zip(r_dirs, c_dirs):
            sr = r+r_dir
            sc = c+c_dir
            if 0 <= sr < n and 0 <= sc < m and board[sr][sc] > 0 and not visited[(sr, sc)]:
                visited[(sr, sc)] = True
                queue.append((sr, sc))
    
    if count < len(glaciers):
        return True
    return False

def solution(n, m, board):
    years = 0
    glaciers = []
    for r in range(n):
        for c in range(m):
            if board[r][c] > 0:
                glaciers.append((r, c))
    
    while glaciers:
        years += 1
        next_board = get_empty_board(n, m)
        for i, g in enumerate(glaciers):
            gr, gc = g
            next_board[gr][gc] = melt(gr, gc, board)
        board = next_board
        
        idx = 0
        while idx < len(glaciers):
            gr, gc = glaciers[idx]
            if next_board[gr][gc] == 0:
                glaciers.pop(idx)
                continue
            idx += 1
            
        if not glaciers:
            years = 0
            break
        if is_multiple(n, m, board, glaciers):
            break
        
    return years

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
result = solution(n, m, board)
print(result)