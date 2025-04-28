from functools import reduce
from math import gcd

def solution(arrayA, arrayB):
    result_a = reduce(gcd, arrayA)
    result_b = reduce(gcd, arrayB)
    
    if not all(b%result_a for b in arrayB):
        result_a = 0
    
    if not all(a%result_b for a in arrayA):
        result_b = 0
        
    return max(result_a, result_b)