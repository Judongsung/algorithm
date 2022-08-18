from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
count = 0
left = 0
right = 0
part_sum = arr[0]
while True:
    if part_sum == m:
        count += 1
        
    if part_sum <= m:
        right += 1
        if right == n:
            break
        part_sum += arr[right]
    else:
        part_sum -= arr[left]
        left += 1
print(count)