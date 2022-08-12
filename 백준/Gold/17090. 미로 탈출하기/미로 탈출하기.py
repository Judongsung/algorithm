from sys import stdin

def is_in_board(r, c):
    return 0 <= r < n and 0 <= c < m

def fill_memo(passed, value):
    for r, c in passed:
        memo[r][c] = value
    return

def find_exit_path(r, c):
    passed_path = set()
    cur_r = r
    cur_c = c
    
    while True:
        if not is_in_board(cur_r, cur_c):
            fill_memo(passed_path, PASSABLE)
            break
        ch = board[cur_r][cur_c]
        tile_memo = memo[cur_r][cur_c]
        passed_path.add((cur_r, cur_c))
        
        if tile_memo == NOT_CHECKED:
            r_dir, c_dir = dirs[ch]
            next_r = cur_r+r_dir
            next_c = cur_c+c_dir
            if (next_r, next_c) in passed_path:
                fill_memo(passed_path, IMPASSABLE)
                break
            cur_r = next_r
            cur_c = next_c
        else:
            fill_memo(passed_path, tile_memo)
            break
    
    return

dirs = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
IMPASSABLE = -1
NOT_CHECKED = 0
PASSABLE = 1

n, m = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(n)]
memo = [[0 for _ in row] for row in board]
for i in range(n):
    for j in range(m):
        if memo[i][j] != NOT_CHECKED:
            continue
        find_exit_path(i, j)

result = 0
for row in memo:
    result += row.count(PASSABLE)
print(result)