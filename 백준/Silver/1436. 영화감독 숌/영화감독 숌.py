n = int(input())

doom = '666'

start = 666 - 1
i = 0
cur = start

while i < n:
    cur += 1
    if doom in str(cur):
        i += 1

print(cur)