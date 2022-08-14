from sys import stdin

IDX = 0
NUM = 1

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
stack = []
nge = ['-1' for _ in range(n)]

for i, n in enumerate(nums):
    while stack and stack[-1][NUM] < n:
        idx, _ = stack.pop()
        nge[idx] = str(n)
    stack.append([i, n])
    
result = ' '.join(nge)
print(result)