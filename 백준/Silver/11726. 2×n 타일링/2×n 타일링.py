n = int(input())
if n == 1:
    result = 1
elif n == 2:
    result = 2
else:
    prev = 1
    cur = 2
    for _ in range(n-2):
        prev, cur = cur, prev+cur
    result = cur%10007
print(result)