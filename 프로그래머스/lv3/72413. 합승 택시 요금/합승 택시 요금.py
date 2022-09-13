from collections import deque

def solution(n, s, a, b, fares):
    min_fare = 10**9
    s -= 1
    a -= 1
    b -= 1
    matrix = [[10**9 for __ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0
    for one, other, fare in fares:
        one -= 1
        other -= 1
        matrix[one][other] = fare
        matrix[other][one] = fare
    queue = deque([s])
    
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                matrix[start][end] = min(matrix[start][end], matrix[start][mid]+matrix[mid][end])
    
    for mid in range(n):
        fare = matrix[s][mid]+matrix[mid][a]+matrix[mid][b]
        min_fare = min(min_fare, fare)
    return min_fare