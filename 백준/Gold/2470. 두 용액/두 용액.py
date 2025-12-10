from sys import stdin


def find_zero_nearest(solutions: list[int]) -> tuple[int]:
    sorted_solutions = sorted(solutions)
    left = 0
    right = len(solutions)-1
    min_left = left
    min_right = right
    min_abs_sum = float('inf')
    
    while left < right:
        sum_sols = sorted_solutions[left]+sorted_solutions[right]
        abs_sum = abs(sum_sols)
        if abs_sum < min_abs_sum:
            min_left = left
            min_right = right
            min_abs_sum = abs_sum
        
        if sum_sols == 0:
            return (sorted_solutions[left], sorted_solutions[right])
            
        if sum_sols < 0:
            left += 1
            
        elif sum_sols > 0:
            right -= 1

    return (sorted_solutions[min_left], sorted_solutions[min_right])
    
n = int(stdin.readline())
sols = list(map(int, stdin.readline().rstrip().split()))
print(*find_zero_nearest(sols))