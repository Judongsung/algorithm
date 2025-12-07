from sys import stdin


def find_sort_average(cur: tuple[int], target: tuple[int], dp: dict[tuple[int], float]) -> float:
    if cur == target:
        return 0.0
        
    if cur in dp:
        return dp[cur]

    sum_expectations = 0.0
    count = 0

    cur_list = list(cur)
    for i, left in enumerate(cur):
        for j in range(i+1, len(cur)):
            right = cur[j]

            if left > right:
                cur_list[i], cur_list[j] = cur_list[j], cur_list[i]

                sum_expectations += find_sort_average(tuple(cur_list), target, dp)
                count += 1

                cur_list[i], cur_list[j] = cur_list[j], cur_list[i]

    if count == 0:
        dp[cur] = 0
    else:
        dp[cur] = 1.0 + (sum_expectations/count)
    return dp[cur]

n = int(stdin.readline())
perm = tuple(map(int, stdin.readline().rstrip().split()))
dp = {}
find_sort_average(perm, sorted(perm), dp)
print(f"{dp[perm]:.6f}")