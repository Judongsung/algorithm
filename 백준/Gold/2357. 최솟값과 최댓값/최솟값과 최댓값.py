from sys import stdin

INF = 10**9

class SegmentTree:
    nums = None
    oper = None
    default_val = 0
    tree = None
    end = -1
    
    def __init__(self, nums, oper, default_val=0):
        self.nums = nums
        self.oper = oper
        self.default_val = default_val
        self.tree = [default_val for _ in range(len(nums)*4)]
        self.end = len(nums)
        self.init_tree()
        
    def init_tree(self, start=1, end=-1, idx=1):
        if end == -1:
            end = self.end
        if start == end:
            self.tree[idx] = [self.nums[start-1]]*2
        else:
            mid = (start+end)//2
            left_value = self.init_tree(start, mid, idx*2)
            right_value = self.init_tree(mid+1, end, idx*2+1)
            self.tree[idx] = self.oper(left_value, right_value)
        return self.tree[idx]
    
    def get_interval_value(self, left, right, idx=1):
        return self._find_interval_value(left, right, 1, self.end)
    
    def _find_interval_value(self, left, right, start, end, idx=1):
        if left > end or right < start:
            return self.default_val
        elif left <= start and end <= right:
            return self.tree[idx]
        else:
            mid = (start+end)//2
            left_value = self._find_interval_value(left, right, start, mid, idx*2)
            right_value = self._find_interval_value(left, right, mid+1, end, idx*2+1)
            return self.oper(left_value, right_value)
        
    def update_value(self, order, value):
        self.nums[order-1] = value
        self.update_tree(order, 1, self.end)
        
    def update_tree(self, order, start, end, idx=1):
        if start <= order <= end:
            if start == end:
                self.tree[idx] = [self.nums[order-1]]*2
            else:
                mid = (start+end)//2
                left_value = self.update_tree(order, start, mid, idx*2)
                right_value = self.update_tree(order, mid+1, end, idx*2+1)
                self.tree[idx] = self.oper(left_value, right_value)
        return self.tree[idx]

n, m = map(int, stdin.readline().split())
nums = [int(stdin.readline()) for _ in range(n)]
oper = lambda a, b:[min(a[0], b[0]), max(a[1], b[1])]
tree = SegmentTree(nums, oper, [INF, 0])
for _ in range(m):
    start, end = map(int, stdin.readline().split())
    result = tree.get_interval_value(start, end)
    print(*result)