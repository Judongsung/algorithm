from sys import stdin

FRONT = 0
MID = 1
END = 2

def solution(n, nodes):
    tree = {}
    for node, c1, c2 in nodes:
        tree[node] = []
        tree[node].append(c1)
        tree[node].append(c2)
    
    front = visit_tree(tree, 'A', FRONT)
    mid = visit_tree(tree, 'A', MID)
    end = visit_tree(tree, 'A', END)
    return [front, mid, end]
    
def visit_tree(tree, cur, mode):
    result = ''
    children = tree[cur]
    if mode == FRONT:
        result += cur
    if children[0] != '.':
        result += visit_tree(tree, children[0], mode)
    if mode == MID:
        result += cur
    if children[1] != '.':
        result += visit_tree(tree, children[1], mode)
    if mode == END:
        result += cur
    return result

n = int(stdin.readline())
nodes = [stdin.readline().split() for _ in range(n)]
result = solution(n, nodes)
for r in result:
    print(r)