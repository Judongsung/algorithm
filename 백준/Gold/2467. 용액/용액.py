from sys import stdin


def bisect_nearest(lst: list, start_left: int, start_right: int, target: int) -> int:
    left = start_left
    right = start_right
    while left <= right:
        mid = (left+right)//2
        if lst[mid] > target:
            right = mid-1
        elif lst[mid] < target:
            left = mid+1
        else:
            return mid

    candidates = []
    if left <= start_right:
        candidates.append(left)
    if right >= start_left:
        candidates.append(right)
    
    return min(candidates, key=lambda x:abs(lst[x]-target))
        

def find_zero_nearest_sum(features: list) -> tuple:
    nearest_left = 0
    nearest_right = 1
    nearest_sum = float('inf')

    for right in range(1, len(features)):
        left = bisect_nearest(features, 0, right-1, -features[right])
        left_feature = features[left]
        right_feature = features[right]
        abs_sum = abs(left_feature+right_feature)
        if abs_sum < nearest_sum:
            nearest_sum = abs_sum
            nearest_left = left_feature
            nearest_right = right_feature

    return nearest_left, nearest_right

n = int(stdin.readline().rstrip())
features = list(map(int, stdin.readline().rstrip().split()))
print(*find_zero_nearest_sum(features))
