from collections import Counter

def get_required_parts(part=-1):
    if type(parts[part]) != Counter:
        total_part_counter = Counter()
    
        if len(parts[part]) == 0:
            total_part_counter[part] += 1
        else:
            for rpart, num in parts[part]:
                part_counter = get_required_parts(rpart)
                for key, val in part_counter.items():
                    total_part_counter[key] += val*num
    
        parts[part] = total_part_counter
    return parts[part]

n = int(input())
m = int(input())
parts = [[] for _ in range(n+1)]
for _ in range(m):
    part, required, num = map(int, input().split())
    parts[part].append([required, num])

result = get_required_parts()
for part, num in sorted(result.items()):
    print(f"{part} {num}")