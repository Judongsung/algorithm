from sys import stdin
        

def find_zero_nearest_sum(features: list) -> tuple:
    nearest_left = 0
    nearest_right = len(features)-1
    nearest_sum = float('inf')
    left = nearest_left
    right = nearest_right

    while left < right:
        cur_sum = features[left]+features[right]
        abs_sum = abs(cur_sum)
        if abs_sum < nearest_sum:
            nearest_sum = abs_sum
            nearest_left = left
            nearest_right = right

        if cur_sum > 0:
            right -= 1
        else:
            left += 1

    return features[nearest_left], features[nearest_right]


n = int(stdin.readline().rstrip())
features = list(map(int, stdin.readline().rstrip().split()))
print(*find_zero_nearest_sum(features))
