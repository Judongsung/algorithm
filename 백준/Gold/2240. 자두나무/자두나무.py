from collections import deque
from typing import List
from sys import stdin

def catch_max_fruits(n: int, fruit_drops: List[int], move: int) -> int:
    now = [0 for _ in range(move+1)]
    prev = [0 for _ in range(move+1)]
    
    for i in range(n):
        drop_pos = [0, 0]
        if fruit_drops[i] == 1:
            drop_pos[0] = 1
        else:
            drop_pos[1] = 1
        prev, now = now, prev
        for i in range(move+1):
            now[i] = 0
        now[0] = prev[0]+drop_pos[0]
        for j in range(1, move+1):
            now[j] = max(prev[j-1]+drop_pos[j%2], prev[j]+drop_pos[j%2])
    
    return max(now)

n, t = map(int, stdin.readline().rstrip().split())
fruit_drops = []
for _ in range(n):
    fruit_drops.append(int(stdin.readline().rstrip()))
    
result = catch_max_fruits(n, fruit_drops, t)
print(result)