from sys import stdin
from collections import deque


def to_bit(num: int) -> int:
    return 1<<num

def find_min_paths(n: int, matrix: list[list[int]]) -> list[list[int]]:
    result = [[el for el in row] for row in matrix]

    for m in range(n):
        for s in range(n):
            for e in range(n):
                result[s][e] = min(result[s][e], result[s][m]+result[m][e])

    return result

def find_min_time(n: int, k: int, paths: list[list[int]]) -> int:
    dp = [[float('inf')]*n for _ in range(to_bit(n))] # dp[visited][position]
    dp[to_bit(k)][k] = 0
    q = deque()
    q.append((to_bit(k), k))

    while q:
        visited, pos = q.popleft()

        for np in range(n):
            b_np = to_bit(np)
            if visited & b_np:
                continue
                
            next_visited = visited|b_np
            
            dp[next_visited][np] = min(dp[next_visited][np], dp[visited][pos]+paths[pos][np])
            q.append((next_visited, np))

    return min(dp[to_bit(n)-1])

n, k = map(int, stdin.readline().rstrip().split())
matrix = []
for _ in range(n):
    row = list(map(int, stdin.readline().rstrip().split()))
    matrix.append(row)

min_paths = find_min_paths(n, matrix)
result = find_min_time(n, k, min_paths)
print(result)