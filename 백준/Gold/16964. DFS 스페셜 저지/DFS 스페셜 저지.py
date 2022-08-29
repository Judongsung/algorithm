from sys import stdin

n = int(stdin.readline())
graph = [set() for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)
visit_order = list(map(int, stdin.readline().split()))
graph[0].add(1)
stack = []
cur = 0

for num in visit_order:
    while stack and num not in graph[cur]:
        cur = stack.pop()
    if num in graph[cur]:
        stack.append(cur)
        cur = num
    elif not stack:
        result = 0
        break
else:
    result = 1
    
print(result)