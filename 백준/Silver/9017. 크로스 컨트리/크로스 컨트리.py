from sys import stdin
from collections import Counter, defaultdict


ATHLETE_PER_TEAM = 6

class TeamInfo:
    def __init__(self, ):
        self.standard_point = 0
        self.fifth_point = 0
        self.checked = 0

    def __lt__(self, other):
        if (self.standard_point < other.standard_point) or \
                (self.standard_point == other.standard_point and self.fifth_point < other.fifth_point):
            return True
        return False

def find_winner(data: list) -> int:
    team_athlete_counter = Counter(data)
    team_infos = defaultdict(TeamInfo)
    
    cur_point = 1
    for team in data:
        if team_athlete_counter[team] < ATHLETE_PER_TEAM:
            continue
        team_info = team_infos[team]
        
        if team_info.checked < 4:
            team_info.standard_point += cur_point
        elif team_info.checked == 4:
            team_info.fifth_point += cur_point
            
        team_info.checked += 1
        cur_point += 1

    return sorted(team_infos, key=lambda x:team_infos[x])[0]

t = int(stdin.readline())
for _ in range(t):
    _ = stdin.readline()
    data = list(stdin.readline().rstrip().split())
    print(find_winner(data))