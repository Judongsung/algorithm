consonants = 'rsefaqtdwczxvg'

def solution(n, s):
    if n == 0 or s[-1] not in consonants:
        return 0
    return 1

n = int(input())
s = input()
result = solution(n, s)
print(result)