from sys import stdin, setrecursionlimit


setrecursionlimit(10**6)

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
HOLE_CH = 'H'
HOLE = 0
INFINITE = -1
NOT_CHECKED = -1

def find_max_count(r: int, c: int, board: list[list[int]], visited: list[list[bool]], memo: list[list[int]]) -> int:
    if (not (0 <= r < rlen and 0 <= c < clen)) or board[r][c] == HOLE:
        return 0
        
    if visited[r][c]:
        return INFINITE
        
    if memo[r][c] != NOT_CHECKED:
        return memo[r][c]

    visited[r][c] = True
    max_count = 0
    move = board[r][c]

    for dr, dc in DIRS:
        nr, nc = r + dr*move, c + dc*move
        count = find_max_count(nr, nc, board, visited, memo)
        
        if count == INFINITE:
            return INFINITE
            
        max_count = max(count, max_count)
    
    visited[r][c] = False
    memo[r][c] = max_count+1
    return memo[r][c]
    
rlen, clen = map(int, stdin.readline().rstrip().split())
board = []

for _ in range(rlen):
    row = list(map(int, list(stdin.readline().rstrip().replace(HOLE_CH, str(HOLE)))))
    board.append(row)

visited = [[False]*clen for _ in range(rlen)]
memo = [[NOT_CHECKED]*clen for _ in range(rlen)]
result = find_max_count(0, 0, board, visited, memo)
print(result)