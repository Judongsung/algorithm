def count_apart(n, board, checked, r, c):
    checked[r][c] = True
    count = 1
    r_dirs = [-1, 0, 0, 1]
    c_dirs = [0, -1, 1, 0]
    
    for r_dir, c_dir in zip(r_dirs, c_dirs):
        nr = r+r_dir
        nc = c+c_dir
        if not (0 <= nr < n and 0 <= nc < n) or (board[nr][nc] == '0' or checked[nr][nc]):
            continue
        count += count_apart(n, board, checked, nr, nc)
    
    return count

def solution(n, board):
    counts = []
    checked = [[False]*n for _ in range(n)]
    
    for r in range(n):
        for c in range(n):
            if board[r][c] == '0' or checked[r][c]:
                continue
            count = count_apart(n, board, checked, r, c)
            counts.append(count)
    
    counts.sort()
    counts.insert(0, len(counts))
    return counts

n = int(input())
board = [input() for _ in range(n)]
result = solution(n, board)
for r in result:
    print(r)