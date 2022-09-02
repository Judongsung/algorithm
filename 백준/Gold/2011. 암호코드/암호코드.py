from sys import stdin

def check_one(s):
    return '1' <= s <= '9'

def check_two(s):
    return 10 <= int(s) <= 26

pw = stdin.readline().rstrip()

memo = [0]*len(pw)
memo[0] += check_one(pw[0])
if len(pw) != 1:
    memo = [0]*len(pw)
    memo[0] += check_one(pw[0])
    if check_one(pw[1]):
        memo[1] += memo[0]
    if check_two(pw[:2]):
        memo[1] += 1

    for i in range(2, len(pw)):
        if check_one(pw[i]):
            memo[i] += memo[i-1]
        if check_two(pw[i-1:i+1]):
            memo[i] += memo[i-2]
    
result = memo[-1]%1000000

print(result)