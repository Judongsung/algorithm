from sys import stdin
from collections import deque

RIPENED = 1
UNRIPENED = 0
NOT_EXIST = -1

m, n = map(int, stdin.readline().rstrip().split())
matrix = []
for _ in range(n):
    line = list(map(int, stdin.readline().rstrip().split()))
    matrix.append(line)

def get_total_ripening_days(rlen:int, clen:int, matrix:list[list[int]]) -> int:
    days = 0
    queue = deque()
    queued = [[False for __ in range(clen)] for _ in range(rlen)]
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    unripened_count = 0

    for r in range(rlen):
        for c in range(clen):
            if matrix[r][c] == RIPENED:
                queue.append((r, c))
                queued[r][c] = True
            elif matrix[r][c] == UNRIPENED:
                unripened_count += 1
    
    while queue:
        next_queue = deque()

        while queue:
            r, c = queue.popleft()

            for r_dir, c_dir in dirs:
                next_r = r+r_dir
                next_c = c+c_dir

                if 0 <= next_r < rlen and 0 <= next_c < clen and\
                        not queued[next_r][next_c] and matrix[next_r][next_c] == UNRIPENED:
                    next_queue.append((next_r, next_c))
                    queued[next_r][next_c] = True
                    unripened_count -= 1
        
        if next_queue:
            queue = next_queue
            days += 1
    
    if unripened_count > 0:
        return -1
    return days

result = get_total_ripening_days(n, m, matrix)
print(result)