def solution(score_info):
    grade_map = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F': 0.0}
    total_score = 0
    total_credit = 0
    for subject, credit, grade in score_info:
        if grade == 'P':
            continue
        credit_num = float(credit)
        total_score += credit_num*grade_map[grade]
        total_credit += credit_num
    
    return total_score/total_credit

score_info = [input().split() for _ in range(20)]
result = solution(score_info)
print(result)