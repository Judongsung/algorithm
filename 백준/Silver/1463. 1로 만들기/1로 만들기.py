from collections import deque

n = int(input())
memo = {}
memo[n] = 0
queue = deque([n])

while queue:
    num = queue.popleft()
    if num == 1:
        print(memo[num])
        break
    next_count = memo[num]+1
    if num%3 == 0 and num//3 not in memo:
        memo[num//3] = next_count
        queue.append(num//3)
    if num%2 == 0 and num//2 not in memo:
        memo[num//2] = next_count
        queue.append(num//2)
    if num-1 not in memo:
        memo[num-1] = next_count
        queue.append(num-1)