import sys

stdin = sys.stdin
sys.setrecursionlimit(2**20)

palindrome_map = {}

def is_palindrome(nums, left, right):
    pair = (left, right)
    if pair in palindrome_map:
        return palindrome_map[pair]
    elif left >= right:
        return 1
    elif nums[left] != nums[right]:
        palindrome_map[pair] = 0
    else:
        palindrome_map[pair] = is_palindrome(nums, left+1, right-1)
    return palindrome_map[pair]

def solution(n, nums, m, mlist):
    for left, right in mlist:
        answer = is_palindrome(nums, left-1, right-1)
        print(answer)
    return

n = int(stdin.readline())
nums = stdin.readline().split()
m = int(stdin.readline())
mlist = [list(map(int, stdin.readline().split())) for _ in range(m)]
solution(n, nums, m, mlist)