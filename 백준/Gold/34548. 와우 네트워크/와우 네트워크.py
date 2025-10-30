from sys import stdin

ONE = 0
OTHER = 1
START_TIME = 2

class DSU:
    def __init__(self, maxnum: int):
        self.parent = list(range(maxnum+1))
        self.size = [1]*(maxnum+1)

    def union(self, x: int, y: int):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.size[x_root] > self.size[y_root]:
                x_root, y_root = y_root, x_root
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        
    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

def get_unstable_score(n: int, max_time: int, connection_info: list[tuple]) -> int:
    dsu = DSU(n)
    score = 0
    conn_count = n
    last_time = 1

    def get_continued_score(cur_time: int, prev_time: int) -> int:
        nonlocal dsu
        return conn_count*(cur_time-prev_time)

    for conn in sorted(connection_info, key=lambda x:x[START_TIME]):
        one, other, start_time = conn[ONE], conn[OTHER], conn[START_TIME]
        one_root = dsu.find(one)
        other_root = dsu.find(other)

        score += get_continued_score(start_time, last_time)
        last_time = start_time

        if one_root != other_root:
            dsu.union(one_root, other_root)
            conn_count -= 1

    else:
        pass
        score += get_continued_score(max_time+1, last_time)
    
    return score

n, m, t = map(int, stdin.readline().rstrip().split())
connection_info = []

for _ in range(m):
    conn = tuple(map(int, stdin.readline().rstrip().split()))
    connection_info.append(conn)

print(get_unstable_score(n, t, connection_info))