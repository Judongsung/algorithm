from sys import stdin

NOT_CHECKED = -1
IMPASSABLE = 0
INF = 10**9

def find_min_cost(cur=0, visited=1):
    if visited == max_bit:
        if matrix[cur][0]:
            return matrix[cur][0]
        else:
            return INF
    elif memo[cur][visited] == NOT_CHECKED:
        min_cost = INF
        
        for i in range(n):
            if matrix[cur][i] != IMPASSABLE and not visited&(1<<i):
                min_cost = min(min_cost, matrix[cur][i]+find_min_cost(i, visited|(1<<i)))
        
        memo[cur][visited] = min_cost
    return memo[cur][visited]

n = int(stdin.readline())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
memo = [[NOT_CHECKED for __ in range(2**n)] for _ in range(n)]
max_bit = 2**n-1
    
min_cost = find_min_cost()

print(min_cost)