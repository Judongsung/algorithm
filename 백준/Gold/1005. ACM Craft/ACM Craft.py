from typing import List, Tuple
from sys import stdin, setrecursionlimit


setrecursionlimit(10**9)

def find_min_buildtime(target:int, times:List[int], orders:List[Tuple[int, int]]) -> int:
    dp = [None for _ in range(len(times))]
    necessaries = [[] for _ in range(len(times))]
    for before, after in orders:
        necessaries[after].append(before)

    def method(cur:int) -> int:
        nonlocal dp
        if dp[cur] == None:
            min_buildtime = 0
            for necessary in necessaries[cur]:
                buildtime = method(necessary)
                min_buildtime = max(buildtime, min_buildtime)
            dp[cur] = min_buildtime+times[cur]
        return dp[cur]
        
    return method(target)

t = int(stdin.readline().rstrip())
for _ in range(t):
    n, k = map(int, stdin.readline().rstrip().split())
    # 건물 번호가 1부터 시작이라 index 0에 더미데이터 삽입
    times = [None]+list(map(int, stdin.readline().rstrip().split()))
    orders = []
    for __ in range(k):
        before, after = map(int, stdin.readline().rstrip().split())
        orders.append((before, after))
    target = int(stdin.readline().rstrip())
    result = find_min_buildtime(target, times, orders)
    print(result)