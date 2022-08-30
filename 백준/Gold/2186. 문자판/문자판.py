from sys import stdin

dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def dfs(r, c, idx=0):
    if memo[r][c][idx] == -1:
        if board[r][c] != word[idx]:
            memo[r][c][idx] = 0
        elif idx == last_idx:
            memo[r][c][idx] = 1
        else:
            next_idx = idx+1
            count = 0

            for r_dir, c_dir in dirs:
                next_r = r
                next_c = c
                for _ in range(k):
                    next_r += r_dir
                    next_c += c_dir
                    if 0 <= next_r < n and 0 <= next_c < m:
                        count += dfs(next_r, next_c, next_idx)
                    else:
                        break

            memo[r][c][idx] = count
            
    return memo[r][c][idx]

n, m, k = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(n)]
word = stdin.readline().rstrip()
memo = [[[-1 for ___ in word] for __ in range(m)] for _ in range(n)]
last_idx = len(word)-1
count = 0

for r in range(n):
    for c in range(m):
        count += dfs(r, c)
            
print(count)