from sys import stdin


def is_possible(distances, router, min_dist) -> bool:
    count = 1
    cur = 0
    for d in distances:
        cur += d
        if cur >= min_dist:
            count += 1
            if count >= router:
                return True
            cur = 0
    return False

def find_max_nearest(pos: list, router: int) -> int:
    distances = []
    sorted_pos = sorted(pos)
    for i in range(len(sorted_pos)-1):
        dist = sorted_pos[i+1]-sorted_pos[i]
        distances.append(dist)
    
    left, right = 0, max(pos)-min(pos)
    while left < right:
        mid = (left+right+1)//2
        if is_possible(distances, router, mid):
            left = mid
        else:
            right = mid-1
            
    return left
    
n, c = map(int, stdin.readline().rstrip().split())
pos = [int(stdin.readline()) for _ in range(n)]
print(find_max_nearest(pos, c))