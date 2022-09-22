from sys import stdin

R = 0
G = 1
B = 2
INF = 10**8

def find_min_cost(first_color):
    memo = [[INF for __ in range(3)] for _ in range(n)]
    memo[0][first_color] = cost[0][first_color]
    
    for i in range(1, n):
        for color in range(3):
            memo[i][color] = cost[i][color]+min([memo[i-1][prev_color] for prev_color in other_colors(color)])
            
    return min([memo[-1][last_color] for last_color in other_colors(first_color)])

def other_colors(color):
    color_set = set([R, G, B])
    color_set.remove(color)
    return color_set

n = int(stdin.readline())
cost = [list(map(int, stdin.readline().split())) for _ in range(n)]
min_cost = INF
for first_color in range(3):
    temp = find_min_cost(first_color)
    if temp < min_cost:
        min_cost = temp
        
print(min_cost)