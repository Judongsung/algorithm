def d(num):
    result = num
    while num:
        num, mod = divmod(num, 10)
        result += mod
    return result

memo = [False for _ in range(10001)]
memo[0] = True

for i in range(1, 10001):
    num = i
    while True:
        num = d(num)
        if num > 10000 or memo[num]:
            break
        memo[num] = True

for i, e in enumerate(memo):
    if not e:
        print(i)