from sys import stdin
from typing import Dict
from collections import deque


START = 1
GOAL = 100
DICE = tuple(n for n in range(6, 0, -1))

def find_min_roll(ladders: Dict[int, int], snakes: Dict[int, int]) -> int:
    goal = GOAL
    visited = [False for _ in range(GOAL+1)] # visited[0]은 더미데이터
    queue = deque()
    queue.append((START, 0))
    visited[START] = True

    while queue:
        pos, roll = queue.popleft()
        next_roll = roll+1

        max_moved = False # 사다리나 뱀이 없이 이동할 수 있는 최대 칸을 이동한 경우
        for n in DICE:
            next_pos = pos+n
            if next_pos >= 100:
                return next_roll
            if visited[next_pos]:
                continue

            if next_pos in ladders:
                next_pos = ladders[next_pos]
            elif next_pos in snakes:
                next_pos = snakes[next_pos]
            elif not max_moved:
                max_moved = True
            else:
                continue
            visited[next_pos] = True
            queue.append((next_pos, next_roll))

    return -1

n, m = map(int, stdin.readline().rstrip().split())
ladders = {}
snakes = {}
for _ in range(n):
    start, end = map(int, stdin.readline().rstrip().split())
    ladders[start] = end
for _ in range(m):
    start, end = map(int, stdin.readline().rstrip().split())
    snakes[start] = end
result = find_min_roll(ladders, snakes)
print(result)