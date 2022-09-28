from sys import stdin

SUM = 0

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
            self.tree[idx] = self.nums[start-1]
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
                self.tree[idx] = self.nums[order-1]
            else:
                mid = (start+end)//2
                left_value = self.update_tree(order, start, mid, idx*2)
                right_value = self.update_tree(order, mid+1, end, idx*2+1)
                self.tree[idx] = self.oper(left_value, right_value)
        return self.tree[idx]

n, m = map(int, stdin.readline().split())
nums = [0 for _ in range(n)]
tree = SegmentTree(nums, lambda a,b:a+b, 0)
for _ in range(m):
    query = list(map(int, stdin.readline().split()))
    if query[0] == SUM:
        if query[1] > query[2]:
            query[1], query[2] = query[2], query[1]
        result = tree.get_interval_value(query[1], query[2])
        print(result)
    else:
        tree.update_value(query[1], query[2])