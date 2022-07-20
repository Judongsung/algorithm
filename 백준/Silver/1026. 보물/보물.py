from sys import stdin

n = int(stdin.readline())
alist = list(map(int, stdin.readline().split()))
blist = list(map(int, stdin.readline().split()))

result = 0
for a_num, b_num in zip(sorted(alist), sorted(blist, reverse=True)):
    result += a_num*b_num
print(result)