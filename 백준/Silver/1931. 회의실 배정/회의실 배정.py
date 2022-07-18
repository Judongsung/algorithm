from sys import stdin

n = int(stdin.readline())
array = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
count = 0
prev_end = 0
array.sort(key=lambda x:x[0])
array.sort(key=lambda x:x[1])

for start, end in array:
    if start >= prev_end:
        prev_end = end
        count += 1
        
print(count)