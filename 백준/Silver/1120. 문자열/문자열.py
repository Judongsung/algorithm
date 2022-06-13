a, b = input().split()
len_a = len(a)
len_b = len(b)
min_difference = len_a
for i in range(len_b-len_a+1):
    difference = 0
    for j in range(len_a):
        if a[j] != b[i+j]:
            difference += 1
    if difference < min_difference:
        min_difference = difference
print(min_difference)