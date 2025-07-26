from sys import stdin
from bisect import insort
from collections import deque


TARGET = 0
NUM = 1

def find_max_delivery(town: int, max_weight: int, boxes: list) -> int:
    result = 0
    cur_weight = 0
    queue = deque()

    for cur, target, num in sorted(boxes, key=lambda x:(x[0],x[1])):
        #print(queue)
        while queue and queue[0][TARGET] <= cur:
            _, weight = queue.popleft()
            cur_weight -= weight
            result += weight
            
        insort(queue, [target, num])
        cur_weight += num
        
        while cur_weight > max_weight:
            last_target, last_num = queue[-1]
            if cur_weight-last_num >= max_weight:
                queue.pop()
                cur_weight -= last_num
            else:
                exceed = cur_weight-max_weight
                queue[-1][NUM] -= exceed
                cur_weight -= exceed
                
    for _, num in queue:
        result += num
    return result


n, c = map(int, stdin.readline().rstrip().split())
m = int(stdin.readline())
boxes = []
for _ in range(m):
    box = list(map(int, stdin.readline().rstrip().split()))
    boxes.append(box)
print(find_max_delivery(n, c, boxes))