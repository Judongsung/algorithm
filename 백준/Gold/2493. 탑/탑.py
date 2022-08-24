from sys import stdin
from collections import deque

NUM = 0
HEIGHT = 1

n = int(stdin.readline())
heights = list(map(int, stdin.readline().split()))
towers = [(i+1, height) for i, height in enumerate(heights)]
stack = deque()
result = ['0' for _ in range(n)]

while towers:
    stack.append(towers.pop())
    while towers and stack and towers[-1][HEIGHT] > stack[-1][HEIGHT]:
        num, _ = stack.pop()
        result[num-1] = str(towers[-1][NUM])

print(' '.join(result))