n, k = map(int, input().split())
values = [int(input()) for _ in range(n)]

values.sort(reverse=True)

result = 0
remains = k
for v in values:
    count, remains = divmod(remains, v)
    result += count
    if not remains:
        break

print(result)