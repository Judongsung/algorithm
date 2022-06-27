def f(a, b):
    return b, a+b

k = int(input())
a = 1
b = 0
for _ in range(k):
    a, b = f(a, b)
print(a, b)