from sys import stdin

INF = 10**9

city_num = int(stdin.readline())
bus_num = int(stdin.readline())
matrix = [[INF for __ in range(city_num)] for _ in range(city_num)]

for _ in range(bus_num):
    start, end, cost = map(int, stdin.readline().split())
    start -= 1
    end -= 1
    if cost < matrix[start][end]:
        matrix[start][end] = cost

for mid in range(city_num):
    for start in range(city_num):
        for end in range(city_num):
            if start != end:
                through_mid = matrix[start][mid]+matrix[mid][end]
                if through_mid < matrix[start][end]:
                    matrix[start][end] = through_mid

for row in matrix:
    temp = list(map(str, row))
    print(' '.join(temp).replace(str(INF), '0'))