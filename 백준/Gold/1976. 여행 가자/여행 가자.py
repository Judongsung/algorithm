from sys import stdin

def union(one, other):
    if one > other:
        one, other = other, one
    parents[find(other)] = find(one)
    return

def find(child):
    if parents[child] != child:
        parents[child] = find(parents[child])
    return parents[child]

n = int(stdin.readline())
m = int(stdin.readline())
parents = [i for i in range(n)]
for i in range(n):
    paths = list(map(int, stdin.readline().split()))
    for j, is_connect in enumerate(paths):
        if is_connect:
            union(i, j)
plan = list(map(lambda x:int(x)-1, stdin.readline().split()))
result = 'YES'

prev = find(plan[0])
for city in plan[1:]:
    cur = find(city)
    if prev != cur:
        result = 'NO'
        break
    prev = cur
    
print(result)