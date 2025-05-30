from sys import stdin, setrecursionlimit
from typing import List


setrecursionlimit(10**6)

def update_ranking(new:int, ranking:List[int]):
    # 이진탐색으로 O(n) -> O(logn) 최적화 가능할듯
    for i, score in enumerate(ranking):
        if new > score:
            ranking.insert(i, new)
            ranking.pop()
            return

def find_max_distance(nodes:List[int]) -> int:
    visited = [False for _ in nodes]
    root = 1
    max_distance = 0
    
    def dfs(cur:int):
        nonlocal nodes, visited, max_distance
        distance_ranking = [0 for _ in range(2)]
        visited[cur] = True

        for num, dist in nodes[cur].items():
            if visited[num]:
                continue
            linked_distance = dist+dfs(num)
            update_ranking(linked_distance, distance_ranking)

        max_distance = max(sum(distance_ranking), max_distance)

        return distance_ranking[0]

    dfs(root)

    return max_distance

v = int(stdin.readline().rstrip())
nodes = [dict() for _ in range(v+1)]
for _ in range(v):
    data = list(map(int, stdin.readline().rstrip().split()))
    num = data[0]
    link_info = data[1:-1]
    
    for i in range(0, len(link_info), 2):
        linked = link_info[i]
        dist = link_info[i+1]
        nodes[num][linked] = dist
        
result = find_max_distance(nodes)
print(result)