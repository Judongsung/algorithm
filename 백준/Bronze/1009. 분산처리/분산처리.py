from sys import stdin

def solution(num, sqr):
    num = num%10
    result = num
    nlist = [num]
    count = 1
    while count < sqr:
        result = (result*num)%10
        if result == num:
            return nlist[(sqr-1)%count]
        nlist.append(result)
        count += 1
    return result

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = solution(a, b)
    if result == 0:
        print(10)
    else:
        print(result)
