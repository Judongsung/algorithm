n = int(input())
max_count = 0
max_num = 0

for i in range(1, n+1):
    a = n
    b = i
    count = 1
    while b >= 0:
        a, b = b, a-b
        count += 1
        
    if count > max_count:
        max_count = count
        max_num = i

print(max_count)
a = n
b = max_num
while a >= 0:
    print(a, end=" ")
    a, b = b, a-b