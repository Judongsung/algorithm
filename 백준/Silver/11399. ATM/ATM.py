import sys

result = 0

n = int(sys.stdin.readline().rstrip())
times = map(int, sys.stdin.readline().rstrip().split())

for i, t in zip(reversed(range(1, n+1)), sorted(times)):
    result += t*i

print(result)