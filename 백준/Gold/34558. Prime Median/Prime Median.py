from math import sqrt
from bisect import bisect, bisect_left
from sys import stdin


def find_primes(maxnum: int) -> list[int]:
    primes = []

    def is_prime(num: int) -> bool:
        for i in range(2, int(sqrt(num))+1):
            if num%i == 0:
                return False
        return True
    
    for i in range(2, maxnum+1):
        if is_prime(i):
            primes.append(i)

    return primes

def find_mid_num(lst: list, left_num: int, right_num: int) -> int:
    left_idx = bisect_left(lst, left_num)
    right_idx = bisect(lst, right_num)
    if right_idx >= len(lst) or lst[right_idx] > right_num:
        right_idx -= 1
    
    if left_idx > right_idx:
        return -1
    elif (right_idx-left_idx)%2 != 0:
        return -1
    else:
        return lst[(right_idx+left_idx)//2]

n = int(stdin.readline())
queries = []
maxnum = 0
for _ in range(n):
    left, right = map(int, stdin.readline().rstrip().split())
    maxnum = max(right, maxnum)
    queries.append((left, right))

primes = find_primes(maxnum)
for left, right in queries:
    print(find_mid_num(primes, left, right))