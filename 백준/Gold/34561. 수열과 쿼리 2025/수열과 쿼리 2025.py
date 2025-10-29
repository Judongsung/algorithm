from sys import stdin
from collections import defaultdict


CHANGE_NUMS = 1
PRINT = 2
MAXNUM = 300_000

class DSU:
    def __init__(self, maxnum: int):
        self.parent = list(range(maxnum+1))
        self.size = [1]*(maxnum+1)

    def union(self, x_root: int, y_root: int):
        if x_root != y_root:
            if self.get_size(x_root) > self.get_size(y_root):
                x_root, y_root = y_root, x_root
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        
    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]
        
class Sequence:
    def __init__(self, sequence: list[int], maxnum):
        self.raw_seq = sequence.copy()
        self.dsu = DSU(maxnum)
        self.val_to_node = {}
        self.node_to_val = {}

        for n in sequence:
            if n not in self.val_to_node:
                self.val_to_node[n] = n
                self.node_to_val[n] = n

        for i in range(1, maxnum+1):
            if i not in self.val_to_node:
                self.val_to_node[i] = i
                self.node_to_val[i] = i

    def change_nums(self, prev: int, changed: int):
        if prev == changed:
            return

        if prev not in self.val_to_node:
            return

        prev_node_root = self.dsu.find(self.val_to_node[prev])

        if changed not in self.val_to_node:
            self.node_to_val[prev_node_root] = changed
            self.val_to_node[changed] = prev_node_root
            del self.val_to_node[prev]
            
        else:
            changed_node_root = self.dsu.find(self.val_to_node[changed])

            if prev_node_root == changed_node_root:
                return

            child_root = prev_node_root
            parent_root = changed_node_root

            if self.dsu.get_size(prev_node_root) > self.dsu.get_size(changed_node_root):
                child_root = changed_node_root
                parent_root = prev_node_root
            
            self.dsu.union(prev_node_root, changed_node_root)

            self.node_to_val[parent_root] = changed
            self.val_to_node[changed] = parent_root

            if child_root in self.node_to_val:
                del self.node_to_val[child_root]
            
            del self.val_to_node[prev]

    def get(self, idx: int) -> int:
        rawnum = self.raw_seq[idx-1] # 1-based to 0-based
        raw_node_root = self.dsu.find(rawnum)
        return self.node_to_val[raw_node_root]

n = int(stdin.readline())
s = list(map(int, stdin.readline().rstrip().split()))
sequence = Sequence(s, MAXNUM)
m = int(stdin.readline())
for _ in range(m):
    query = list(map(int, stdin.readline().rstrip().split()))
    if query[0] == CHANGE_NUMS:
        sequence.change_nums(query[1], query[2])
    elif query[0] == PRINT:
        print(sequence.get(query[1]))
    else:
        pass