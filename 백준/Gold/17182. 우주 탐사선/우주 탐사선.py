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
    dp = [[-1]*n for _ in range(to_bit(n))] # dp[visited][position]

    def dfs(visited: int, pos: int) -> int:
        if visited == to_bit(n)-1:
            return 0

        if dp[visited][pos] != -1:
            return dp[visited][pos]

        min_time = float('inf')

        for np in range(n):
            if not (visited & to_bit(np)):
                min_time = min(min_time, paths[pos][np]+dfs(visited|to_bit(np), np))
        
        dp[visited][pos] = min_time
        return min_time

    return dfs(to_bit(k), k)

n, k = map(int, stdin.readline().rstrip().split())
matrix = []
for _ in range(n):
    row = list(map(int, stdin.readline().rstrip().split()))
    matrix.append(row)

min_paths = find_min_paths(n, matrix)
result = find_min_time(n, k, min_paths)
print(result)