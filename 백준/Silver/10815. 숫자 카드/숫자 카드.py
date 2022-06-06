from sys import stdin

def is_include(nlist, target, start=None, end=None):
    if not start and not end:
        start = 0
        end = len(nlist)-1
    elif start > end:
        return '0'
    
    mid = round((start+end)/2)
    if nlist[mid] == target:
        return '1'
    elif nlist[mid] > target:
        return is_include(nlist, target, start, mid-1)
    else:
        return is_include(nlist, target, mid+1, end)
    
def solution(n, nlist, m, mlist):
    result = []
    sorted_nlist = sorted(nlist)
    
    for target in mlist:
        r = is_include(sorted_nlist, target)
        result.append(r)
    return result

n = int(stdin.readline())
nlist = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
mlist = list(map(int, stdin.readline().split()))
result = solution(n, nlist, m, mlist)
print(' '.join(result))