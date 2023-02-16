from sys import stdin

n = int(stdin.readline())
matrix = [[0 for __ in range(n)] for _ in range(n)]
while True:
    a, b = map(int, stdin.readline().split())
    if a == b == -1:
        break
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

for mid in range(n):
    for start in range(n):
        for end in range(n):
            if start != end and matrix[start][mid] != 0 and matrix[mid][end] != 0 and (matrix[start][end] == 0 or matrix[start][mid]+matrix[mid][end] < matrix[start][end]):
                matrix[start][end] = matrix[start][mid]+matrix[mid][end]
                
min_score = n
min_list = []
for i in range(n):
    score = max(matrix[i])
    if score == min_score:
        min_list.append(i+1)
    elif score < min_score:
        min_score = score
        min_list = [i+1]
        
print(min_score, len(min_list))
print(*min_list)