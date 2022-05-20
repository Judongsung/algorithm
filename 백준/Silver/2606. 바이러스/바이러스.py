# 백준 2606 바이러스

def bfs(relations, root):
    visited = [0 for _ in relations]
    queue = []
    queue.append(root)
    visited[root] = 1
    count = 0
    while queue:
        com = queue.pop(0)
        for r in relations[com]:
            if visited[r] == 0:
                count += 1
                queue.append(r)
                visited[r] = 1
    
    return count

computers = int(input())
relations = [None] + [[] for _ in range(computers)]
for _ in range(int(input())):
    c1, c2 = map(int, input().split())
    relations[c1].append(c2)
    relations[c2].append(c1)

result = bfs(relations, 1)
print(result)