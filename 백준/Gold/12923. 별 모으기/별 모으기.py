from sys import stdin
from collections import deque
from heapq import heappush, heappop


IDX = 2
A_REQ = 1
B_REQ = 0
NOT_CLEAR = 0
HALF_CLEAR = 1
ALL_CLEAR = 2
IMPOSSIBLE = -1

def find_min_play(n: int, stages: list[tuple[int]]) -> int:
    count = 0
    stars = 0
    indexed_stages = [{IDX: i, A_REQ: stage[0], B_REQ: stage[1]} for i, stage in enumerate(stages)]
    indexed_stages.sort(key=lambda x:x[A_REQ])
    sidx = 0
    aq = []
    bq = deque(sorted(indexed_stages, key=lambda x:x[B_REQ]))
    clear = [NOT_CLEAR]*n

    while bq:
        while sidx < n and indexed_stages[sidx][A_REQ] <= stars:
            heappush(aq, (-indexed_stages[sidx][B_REQ], indexed_stages[sidx][A_REQ], indexed_stages[sidx][IDX]))
            sidx += 1
        
        if bq and bq[0][B_REQ] <= stars:
            idx = bq.popleft()[IDX]
            
            stars += 1
            if clear[idx] == NOT_CLEAR:
                stars += 1
                
            clear[idx] = ALL_CLEAR
            count += 1
            continue

        while aq and clear[aq[0][IDX]] != NOT_CLEAR:
            heappop(aq)

        if aq and aq[0][A_REQ] <= stars:
            idx = heappop(aq)[IDX]
            
            stars += 1
            clear[idx] = HALF_CLEAR
            count += 1
            continue

        return IMPOSSIBLE

    return count
            
n = int(stdin.readline())
stages = []

for _ in range(n):
    a, b = map(int, stdin.readline().rstrip().split())
    stages.append((a, b))

result = find_min_play(n, stages)
if result == IMPOSSIBLE:
    print('Too Bad')
else:
    print(result)