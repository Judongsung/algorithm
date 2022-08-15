from sys import stdin

n = int(stdin.readline())
goal = [int(stdin.readline()) for _ in range(n)]
nums = [i for i in range(n, 0, -1)]
stack = []
opers = []

for target in goal:
    while nums and target >= nums[-1]:
        popped = nums.pop()
        stack.append(popped)
        opers.append('+')
    if stack and stack[-1] == target:
        stack.pop()
        opers.append('-')
    else:
        opers = ['NO']
        break

for op in opers:
    print(op)