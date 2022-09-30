from sys import stdin

INF = 1001

def find_max_increase(cur=0):
    if memo[cur] == 0:
        max_increase = 0
        increase_min_num = INF
        for after in range(cur+1, n):
            if nums[cur] < nums[after] < increase_min_num:
                increase = find_max_increase(after)
                increase_min_num = nums[after]
                if increase > max_increase:
                    max_increase = increase
        memo[cur] = max_increase+1
    return memo[cur]

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
memo = [0 for _ in range(n)]
for i, num in enumerate(nums):
    find_max_increase(i)
print(max(memo))