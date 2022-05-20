# 백준 2178 미로 탐색

def bfs(n, m, board):
    visited = [[0 for _ in row] for row in board]
    queue = []
    queue.append([0, 0, 1])
    visited[0][0] = 1
    while queue:
        r, c, count = queue.pop(0)
        if r == n-1 and c == m-1:
            return count
        if 0 <= r-1 < n and 0 <= c < m and board[r-1][c] == "1" and visited[r-1][c] == 0:
            visited[r-1][c] = 1
            queue.append([r-1, c, count+1])
        if 0 <= r < n and 0 <= c-1 < m and board[r][c-1] == "1" and visited[r][c-1] == 0:
            visited[r][c-1] = 1
            queue.append([r, c-1, count+1])
        if 0 <= r < n and 0 <= c+1 < m and board[r][c+1] == "1" and visited[r][c+1] == 0:
            visited[r][c+1] = 1
            queue.append([r, c+1, count+1])
        if 0 <= r+1 < n and 0 <= c < m and board[r+1][c] == "1" and visited[r+1][c] == 0:
            visited[r+1][c] = 1
            queue.append([r+1, c, count+1])

n, m = map(int, input().split())
board = [input() for _ in range(n)]
result = bfs(n, m, board)
print(result)