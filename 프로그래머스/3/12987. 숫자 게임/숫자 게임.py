def get_score():
    pass
    return memo


def solution(A, B):
    answer = 0
    sorted_a = sorted(A)
    sorted_b = sorted(B)
    pa = 0
    
    for b_card in sorted_b:
        if sorted_a[pa] < b_card:
            answer += 1
            pa += 1
    
    return answer