n = int(input())
count = 0
for num in range(1, n+1):
    if num < 100:
        count += 1
    else:
        str_num = str(num)
        sub = int(str_num[0])-int(str_num[1])
        for i in range(1, len(str_num)-1):
            if int(str_num[i])-int(str_num[i+1]) != sub:
                break
        else:
            count += 1
print(count)