# 백준 2644 촌수계산

class person:
    def __init__(self, ):
        self.relations = []

def dfs(people, a, b):
    visited = [0 for _ in people]
    queue = []
    queue.append([a, 0])
    visited[a] = 1
    
    while queue:
        cur, count = queue.pop(0)
        if cur == b:
            return count
        
        for r in people[cur].relations:
            if visited[r] == 0:
                queue.insert(0, [r, count+1])
                visited[r] = 1
    
    return -1
    
        
n = int(input())
people = [None] + [person() for _ in range(n)]
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    parent, child = map(int, input().split())
    people[parent].relations.append(child)
    people[child].relations.append(parent)

print(dfs(people, a, b))