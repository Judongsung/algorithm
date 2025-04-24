def solution(scores):
    num_scores = [[i, score] for i, score in enumerate(scores)]
    no_incentives = set()
    
    max_cowalker = 0
    prev_attitude = 0
    sorted_by_cowalker = sorted(num_scores, key=lambda x:x[1][1])
    for num, score in sorted(sorted_by_cowalker, key=lambda x:x[1][0], reverse=True):
        if score[1] < max_cowalker:
            if num == 0:
                return -1
            no_incentives.add(num)
        
        max_cowalker = max(max_cowalker, score[1])
    
    rank = 1
    prev_score_sum = 0
    for num, score in sorted(num_scores, key=lambda x:sum(x[1]), reverse=True):
        if num in no_incentives:
            continue
        elif num == 0:
            return rank
        elif sum(score) != prev_score_sum:
            rank += 1