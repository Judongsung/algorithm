from sys import stdin

def find_parent(network, p):
    if p == network[p]:
        return p
    return find_parent(network, network[p])
            
def union(network, count, p1, p2):
    p1_parent = find_parent(network, p1)
    p2_parent = find_parent(network, p2)
    if p1_parent == p2_parent:
        return
    if p1_parent < p2_parent:
        network[p1_parent] = network[p2_parent]
        count[p2_parent] += count[p1_parent]
    else:
        network[p2_parent] = network[p1_parent]
        count[p1_parent] += count[p2_parent]
        
n = int(stdin.readline())
for _ in range(n):
    network = {}
    count = {}
    f = int(stdin.readline())
    for __ in range(f):
        p1, p2 = stdin.readline().split()
        if p1 not in network:
            network[p1] = p1
            count[p1] = 1
        if p2 not in network:
            network[p2] = p2
            count[p2] = 1
        union(network, count, p1, p2)
        print(count[find_parent(network, p1)])