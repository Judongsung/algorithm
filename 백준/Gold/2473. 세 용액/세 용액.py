from sys import stdin


def find_zero_nearest(n: int, solutions: list[int]) -> tuple[int]:
    sorted_solutions = sorted(solutions)
    min_abs_sum = float('inf')
    result = None
    
    for left in range(n-2):
        mid = left+1
        right = n-1

        while mid < right:
            sum_sols = sorted_solutions[left]+sorted_solutions[mid]+sorted_solutions[right]
            abs_sum = abs(sum_sols)
            if abs_sum < min_abs_sum:
                min_abs_sum = abs_sum
                result = (sorted_solutions[left], sorted_solutions[mid], sorted_solutions[right])
            
            if sum_sols == 0:
                return result
                
            if sum_sols < 0:
                mid += 1
                
            elif sum_sols > 0:
                right -= 1

    return result

n = int(stdin.readline())
sols = list(map(int, stdin.readline().rstrip().split()))
print(*find_zero_nearest(n, sols))