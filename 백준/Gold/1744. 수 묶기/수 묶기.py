from sys import stdin

def read_num():
    numstr = stdin.readline().rstrip()
    return int(numstr)

def sum_multiple_of_pairs(numlist):
    result = 0
    
    for a, b in zip(range(0, len(numlist), 2), range(1, len(numlist), 2)):
        result += numlist[a]*numlist[b]
        
    return result

result = 0
negatives = []
positives = []
has_zero = False

n = read_num()
for _ in range(n):
    num = read_num()
    if num < 0:
        negatives.append(num)
    elif num > 1:
        positives.append(num)
    elif num == 1:
        result += 1
    else:
        has_zero = True

negatives.sort()
positives.sort(reverse=True)

result += sum_multiple_of_pairs(negatives)
result += sum_multiple_of_pairs(positives)

if len(negatives)%2 > 0 and not has_zero:
    result += negatives[-1]
if len(positives)%2 > 0:
    result += positives[-1]
    
print(result)