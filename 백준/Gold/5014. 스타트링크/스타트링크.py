# 백준 5014 스타트링크

def bfs(f, s, g, u, d):
    if s == g:
        return 0
    visited = [-1 for _ in range(f+1)]
    queue = []
    queue.append([s, 0])
    while queue:
        cur_s, cur_c = queue.pop(0)
        if 0 < cur_s <= f and visited[cur_s] == -1:
            visited[cur_s] = cur_c
            if cur_s+u == g:
                return cur_c+1
            else:
                queue.append([cur_s+u, cur_c+1])
            if cur_s-d == g:
                return cur_c+1
            else:
                queue.append([cur_s-d, cur_c+1])
    
    return "use the stairs"
    

f, s, g, u, d = map(int, input().split())
result = bfs(f, s, g, u, d)
print(result)