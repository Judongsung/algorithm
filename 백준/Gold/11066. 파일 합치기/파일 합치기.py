from sys import stdin

INF = 10**8

def find_min_cost(start, end):
    if memo[start][end] == -1:
        min_cost = INF
        for mid in range(start, end):
            cost = find_min_cost(start, mid)+find_min_cost(mid+1, end)
            if cost < min_cost:
                min_cost = cost
        memo[start][end] = min_cost+size_sum[end]-size_sum[start-1]
    return memo[start][end]

t = int(stdin.readline())
for _ in range(t):
    k = int(stdin.readline())
    pages = list(map(int, stdin.readline().split()))
    size_sum = [0 for _ in range(k+1)]
    size_sum[0] = pages[0]
    for i in range(1, k):
        size_sum[i] = size_sum[i-1]+pages[i]
    memo = [[-1 for __ in range(k)] for _ in range(k)]
    for i in range(k):
        memo[i][i] = 0
    result = find_min_cost(0, k-1)
    print(result)