from sys import stdin

def find_path(matrix, visited, start, cur):
    for i, el in enumerate(matrix[cur]):
        if el == '1' and not visited[start][i]:
            matrix[start][i] = '1'
            visited[start][i] = True
            find_path(matrix, visited, start, i)
                
def solution(n, matrix):
    result = [row.copy() for row in matrix]
    visited = [[False]*n for _ in range(n)]
    
    for i in range(n):
        find_path(result, visited, i, i)
    
    return result

n = int(stdin.readline())
matrix = [stdin.readline().split() for _ in range(n)]
result = solution(n, matrix)
for row in result:
    print(" ".join(row))