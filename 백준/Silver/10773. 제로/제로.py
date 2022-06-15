from sys import stdin

arr = []
k = int(stdin.readline())
for _ in range(k):
    n = int(stdin.readline())
    if n == 0:
        arr.pop()
    else:
        arr.append(n)
print(sum(arr))