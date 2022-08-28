from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

def dfs(num):
    if visited[num]:
        return 0
    visited[num] = True
    count = 0
    
    for friend in graph[num]:
        temp = dfs(friend)
        if temp >= 5:
            count = temp
            break
        count = max(count, temp)
    
    visited[num] = False
    return count+1

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]
result = 0
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
for num in range(n):
    if dfs(num) >= 5:
        result = 1
        break
        
print(result)