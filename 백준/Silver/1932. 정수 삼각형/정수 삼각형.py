from sys import stdin


def find_max_path(triangle: list[list[int]]) -> int:
    dp = [[0]*len(floor) for floor in triangle]
    dp[0][0] = triangle[0][0]

    for i, floor in enumerate(dp[:-1]):
        for j, num in enumerate(floor):
            for k in range(j, j+2):
                if num+triangle[i+1][k] > dp[i+1][k]:
                    dp[i+1][k] = num+triangle[i+1][k]

    return max(dp[-1])
        
n = int(stdin.readline())
triangle = []

for _ in range(n):
    floor = list(map(int, stdin.readline().rstrip().split()))
    triangle.append(floor)

result = find_max_path(triangle)
print(result)