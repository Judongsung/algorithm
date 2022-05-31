from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

def dfs(tree, dp, visited, node):
    visited[node] = True
    
    for conn in tree[node]:
        if visited[conn]:
            continue
        dfs(tree, dp, visited, conn)
        dp[node][0] += dp[conn][1]
        dp[node][1] += min(dp[conn])

def solution(n, tree):
    dp = [None]+[[0, 1] for _ in range(n)]
    visited = [False for _ in range(n+1)]
    
    dfs(tree, dp, visited, 1)
    return min(dp[1])

n = int(stdin.readline())
tree = [None]+[[] for _ in range(n)]
for _ in range(n-1):
    n1, n2 = map(int, stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)
result = solution(n, tree)
print(result)