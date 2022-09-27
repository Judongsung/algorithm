from sys import stdin

DEFAULT_VALUE = 10**9

def make_segment_tree(start, end, cur=1):
    if start == end:
        tree[cur] = nums[start]
    else:
        mid = (start+end)//2
        left_value = make_segment_tree(start, mid, cur*2)
        right_value = make_segment_tree(mid+1, end, cur*2+1)
        tree[cur] = oper(left_value, right_value)
    return tree[cur]

def find_interval_value(start, end, left, right, cur=1):
    if left > end or right < start:
        return DEFAULT_VALUE
    elif left <= start and end <= right:
        return tree[cur]
    else:
        mid = (start+end)//2
        left_value = find_interval_value(start, mid, left, right, cur*2)
        right_value = find_interval_value(mid+1, end, left, right, cur*2+1)
        return oper(left_value, right_value)

n, m = map(int, stdin.readline().split())
nums = [int(stdin.readline()) for _ in range(n)]
tree = [0 for _ in range(n*4)]
oper = lambda a, b:min(a, b)
make_segment_tree(0, n-1)
for _ in range(m):
    left, right = map(int, stdin.readline().split())
    value = find_interval_value(1, n, left, right)
    print(value)