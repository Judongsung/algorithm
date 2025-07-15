from sys import stdin
from math import ceil

def find_min_height(n: int, positions: list) -> int:
    if len(positions) == 1:
        return max(positions[0], n-positions[0])

    min_height = max(positions[0], n-positions[-1])
    for i, left in enumerate(positions[:-1]):
        right = positions[i+1]
        min_height = max(ceil((right-left)/2), min_height)
    
    return min_height

n = int(stdin.readline())
m = int(stdin.readline())
positions = list(map(int, stdin.readline().rstrip().split()))
print(find_min_height(n, positions))