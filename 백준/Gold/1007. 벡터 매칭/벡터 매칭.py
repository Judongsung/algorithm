from itertools import combinations
from math import sqrt
from typing import List, Tuple
from sys import stdin


X = 0
Y = 1

def find_min_vector_sum_distance(points:List[Tuple[int, int]]) -> float:
    min_distance_pow = float('inf')
    vector_num = len(points)//2
    used = [False for _ in points]
    total_vector_sum = [0, 0]
    for x, y in points:
        total_vector_sum[X] += x
        total_vector_sum[Y] += y

    def dfs(x_sum=0, y_sum=0, remains=vector_num, start=0) -> None:
        nonlocal min_distance_pow, used
        
        if not remains:
            distance_pow = (total_vector_sum[X]-2*x_sum)**2+(total_vector_sum[Y]-2*y_sum)**2
            min_distance_pow = min(distance_pow, min_distance_pow)
            return
        elif remains > len(points)-start:
            return

        for i in range(start, len(points)):
            if used[i]:
                continue
            used[i] = True
            dfs(x_sum+points[i][X], y_sum+points[i][Y], remains-1, i+1)
            used[i] = False

    dfs()
    return sqrt(min_distance_pow)

t = int(stdin.readline().rstrip())

for _ in range(t):
    n = int(stdin.readline().rstrip())
    points = []
    for __ in range(n):
        x, y = map(int, stdin.readline().rstrip().split())
        points.append((x, y))

    result = find_min_vector_sum_distance(points)
    print(result)