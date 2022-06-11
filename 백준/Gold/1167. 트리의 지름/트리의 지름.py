from sys import stdin

total_max_distance = 0

def solution(v, node_infos):
    tree = create_tree(v, node_infos)
    dfs(tree, 1, None)
    return total_max_distance

def create_tree(v, node_infos):
    tree = [[] for _ in range(v+1)]
    for ninfo in node_infos:
        node = ninfo[0]
        cursor = 1
        while ninfo[cursor] != -1:
            other = ninfo[cursor]
            distance = ninfo[cursor+1]
            tree[node].append((other, distance))
            cursor += 2
    return tree

def dfs(tree, cur, parent):
    global total_max_distance
    cur_max_distance = 0
    
    for conn, dist in tree[cur]:
        if conn == parent:
            continue
        temp = dfs(tree, conn, cur)+dist
        if temp+cur_max_distance > total_max_distance:
            total_max_distance = temp+cur_max_distance
        if temp > cur_max_distance:
            cur_max_distance = temp
        
    return cur_max_distance

v = int(stdin.readline())
node_infos = [list(map(int, stdin.readline().split())) for _ in range(v)]
result = solution(v, node_infos)
print(result)