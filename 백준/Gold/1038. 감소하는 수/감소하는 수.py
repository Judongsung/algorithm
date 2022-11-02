from collections import defaultdict

digit_decrease_dict = defaultdict(list)
digit_decrease_dict[1] = list(map(str, range(10)))
n = int(input())

if n == 0:
    result = 0
elif n < 10:
    result = digit_decrease_dict[1][n]
else:
    n -= 9
    cur_digit = 2

    while n > 0:
        for i in range(1, 10):
            front = str(i)
            for el in digit_decrease_dict[cur_digit-1]:
                if front > el[0]:
                    digit_decrease_dict[cur_digit].append(front+el)
                    n -= 1
                    if n == 0:
                        result = front+el
                        break
            if n == 0:
                break
        cur_digit += 1
        if cur_digit > 11:
            result = -1
            break

print(result)