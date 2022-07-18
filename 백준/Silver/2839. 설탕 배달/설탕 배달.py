n = int(input())
five_count, remains = divmod(n, 5)

while remains%3 > 0:
    if five_count == 0:
        result = -1
        break
    five_count -= 1
    remains += 5
else:
    three_count = remains//3
    result = five_count+three_count

print(result)