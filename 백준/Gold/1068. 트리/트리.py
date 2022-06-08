from sys import stdin

PARENT = 0
CHILDREN = 1

def create_tree(n, node_infos):
    tree = [[None, []] for _ in range(n)]
    
    for node, parent in enumerate(node_infos):
        tree[node][PARENT] = parent
        if parent == -1:
            root = node
            continue
        tree[parent][CHILDREN].append(node)
    
    return tree, root

def remove_tree_node(tree, remove_node):
    remove_parent = tree[remove_node][PARENT]
    tree[remove_parent][CHILDREN].remove(remove_node)
    return

def solution(n, nodes, removed_node):
    tree, root = create_tree(n, nodes)
    if removed_node == root:
        return 0
    remove_tree_node(tree, removed_node)
    
    queue = [root]
    count = 0
    while queue:
        node = queue.pop()
        if not tree[node][CHILDREN]:
            count += 1
            continue
        for child in tree[node][CHILDREN]:
            queue.append(child)
    
    return count

n = int(stdin.readline())
nodes = list(map(int, stdin.readline().split()))
removed_node = int(stdin.readline())
result = solution(n, nodes, removed_node)
print(result)