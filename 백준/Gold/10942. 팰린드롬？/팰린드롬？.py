from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**5)

def is_palindrome(nums, left, right):
    if palindrome_map[left][right] != -1:
        return palindrome_map[left][right]
    elif left >= right:
        palindrome_map[left][right] = 1
    elif nums[left] != nums[right]:
        palindrome_map[left][right] = 0
    else:
        palindrome_map[left][right] = is_palindrome(nums, left+1, right-1)
    return palindrome_map[left][right]

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
palindrome_map = [[-1 for __ in range(n)] for _ in range(n)]
m = int(stdin.readline())
for _ in range(m):
    left, right = map(int, stdin.readline().split())
    answer = is_palindrome(nums, left-1, right-1)
    print(answer)