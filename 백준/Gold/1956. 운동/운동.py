from sys import stdin

INF = 10**9

v, e = map(int, stdin.readline().split())
matrix = [[INF for __ in range(v)] for _ in range(v)]
for _ in range(e):
    start, end, distance = map(int, stdin.readline().split())
    matrix[start-1][end-1] = distance
    
for mid in range(v):
    for start in range(v):
        for end in range(v):
            through_mid = matrix[start][mid]+matrix[mid][end]
            if through_mid < matrix[start][end]:
                matrix[start][end] = through_mid
                
min_cycle = INF
for i in range(v):
    if matrix[i][i] < min_cycle:
        min_cycle = matrix[i][i]
        
if min_cycle == INF:
    min_cycle = -1
        
print(min_cycle)