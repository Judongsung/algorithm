from sys import stdin

INF = 1001

def find_max_increase(cur=0):
    if memo[cur] == 0:
        max_inc_nums = []
        increase_min_num = INF
        for after in range(cur+1, n):
            if nums[cur] < nums[after] < increase_min_num:
                inc_nums = find_max_increase(after)
                increase_min_num = nums[after]
                if len(inc_nums) > len(max_inc_nums):
                    max_inc_nums = inc_nums
        memo[cur] = [nums[cur]]+max_inc_nums
    return memo[cur]

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
memo = [0 for _ in range(n)]
max_inc_nums = []
for i, num in enumerate(nums):
    inc_nums = find_max_increase(i)
    if len(inc_nums) > len(max_inc_nums):
        max_inc_nums = inc_nums
print(len(max_inc_nums))
print(*max_inc_nums)