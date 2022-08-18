from sys import stdin

while True:
    data = stdin.readline()
    if data == '':
        break
    x = int(data)*10000000
    n = int(stdin.readline())
    lego_list = [int(stdin.readline()) for _ in range(n)]
    lego_list.sort()
    lighter = 0
    heavier = n-1

    while lighter < heavier:
        sum_two = lego_list[lighter]+lego_list[heavier]
        if sum_two == x:
            result = 'yes %d %d'%(lego_list[lighter], lego_list[heavier])
            break
        elif sum_two < x:
            lighter += 1
        else:
            heavier -= 1
    else:
        result = 'danger'

    print(result)