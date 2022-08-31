from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

def find_max_radius(cur):
    global max_radius
    max_length = 0
    second_max_length = 0
    
    for connect, weight in graph[cur]:
        length = find_max_radius(connect)+weight
        if length > max_length:
            second_max_length = max_length
            max_length = length
        elif length > second_max_length:
            second_max_length = length
            
    radius = max_length+second_max_length
    max_radius = max(max_radius, radius)
    return max_length

n = int(stdin.readline())
graph = [[] for _ in range(n+1)]
max_radius = 0
for _ in range(n-1):
    parent, child, weight = map(int, stdin.readline().split())
    graph[parent].append((child, weight))
    
find_max_radius(1)
print(max_radius)