import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

string = input()

prefix_sum_list = [None for _ in range(len(string)+1)]
prefix_sum_list[0] = defaultdict(int)
prefix_sum_list[0][string[0]] = 1
prefix_sum_list[-1] = defaultdict(int)

for i, ch in zip(range(1, len(string)), string[1:]):
    index_dict = prefix_sum_list[i-1].copy()
    index_dict[ch] += 1
    prefix_sum_list[i] = index_dict
    
n = int(input())

for _ in range(n):
    query = input().split()
    ch = query[0]
    left = int(query[1])
    right = int(query[2])
    
    result = prefix_sum_list[right][ch]-prefix_sum_list[left-1][ch]
    print(result)