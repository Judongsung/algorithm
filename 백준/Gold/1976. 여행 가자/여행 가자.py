from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
for i in range(n):
    matrix[i][i] = 1
plan = list(map(int, stdin.readline().split()))
result = 'YES'

for mid in range(n):
    for start in range(n):
        for end in range(n):
            if matrix[start][mid] and matrix[mid][end]:
                matrix[start][end] = 1
                
cur = plan[0]-1
for city in plan[1:]:
    city -= 1
    if not matrix[cur][city]:
        result = 'NO'
        break
    cur = city
    
print(result)