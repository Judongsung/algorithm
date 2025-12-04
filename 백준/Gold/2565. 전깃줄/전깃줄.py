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

def find_min_disconnections(connections: list[tuple[int]]) -> int:
    nums = []
    
    for conn in sorted(connections):
        nums.append(conn[1])

    return len(nums)-find_lis_length(nums)

n = int(stdin.readline())
conns = []
for _ in range(n):
    conn = tuple(map(int, stdin.readline().rstrip().split()))
    conns.append(conn)

result = find_min_disconnections(conns)
print(result)