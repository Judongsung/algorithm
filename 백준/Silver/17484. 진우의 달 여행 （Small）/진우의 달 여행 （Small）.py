from sys import stdin


def find_min_cost(matrix: list, n: int, m: int) -> int:
    dirs = (-1, 0, 1)
    memo = [[cost for _ in dirs] for cost in matrix[0]]
    
    for r, line in enumerate(matrix[1:]):
        next_memo = [[float('inf') for _ in dirs] for _ in range(m)]

        for loc, costs in enumerate(memo):
            for i, d in enumerate(dirs):
                if not (0 <= loc+d < m):
                    continue
                for prev_d, cost in zip(dirs, costs):
                    if d == prev_d:
                        continue
                    next_memo[loc+d][i] = min(next_memo[loc+d][i], cost+line[loc+d])
        memo = next_memo
        
    return min([cost for costs in memo for cost in costs])

n, m = map(int, stdin.readline().rstrip().split())
matrix = []
for _ in range(n):
    line = list(map(int, stdin.readline().rstrip().split()))
    matrix.append(line)
print(find_min_cost(matrix, n, m))