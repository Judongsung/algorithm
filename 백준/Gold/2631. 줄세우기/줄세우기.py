from sys import stdin


def find_lis_length(nums: list[int]) -> int:
    result = 0
    dp = [0]*len(nums)
    dp[0] = 1

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[j], dp[i])
                
        dp[i] += 1
        result = max(dp[i], result)
    
    return result

def find_min_move_for_order(nums: list[int]) -> int:
    return len(nums)-find_lis_length(nums)

n = int(stdin.readline())
nums = [0]*n
for i in range(n):
    nums[i] = int(stdin.readline())
result = find_min_move_for_order(nums)
print(result)