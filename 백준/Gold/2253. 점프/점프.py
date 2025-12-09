from sys import stdin
from collections import deque


IMPOSSIBLE = -1

def find_min_jump(goal: int, disabled_rocks: set[int]) -> int:
    q = deque([(1, 0, 0)]) # location, jump_count, jump_distance
    visited = set((1, 0)) # location, jump_distance

    while q:
        loc, count, dist = q.popleft()

        for nd in range(dist+1, dist-2, -1):
            next_loc = loc+nd
            if next_loc == goal:
                return count+1
            if not (loc < next_loc < goal) or next_loc in disabled_rocks or (next_loc, nd) in visited:
                continue

            q.append((next_loc, count+1, nd))
            visited.add((next_loc, nd))

    return IMPOSSIBLE

n, m = map(int, stdin.readline().rstrip().split())
disabled_rocks = set()
for _ in range(m):
    small_rock = int(stdin.readline())
    disabled_rocks.add(small_rock)

print(find_min_jump(n, disabled_rocks))