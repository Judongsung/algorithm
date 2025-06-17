from dataclasses import dataclass
from typing import List
from sys import stdin, stdout


LEVEL_GAP = 10

@dataclass(order=True)
class Player:
    nickname: str
    level: int

class Room:
    def __init__(self, master: Player, capacity):
        self.players = [master]
        master_level = master.level
        self.min_level = master_level-LEVEL_GAP
        self.max_level = master_level+LEVEL_GAP
        self.capacity = capacity

    def is_joinable(self, player: Player) -> bool:
        level = player.level
        return not self.is_full() and self.min_level <= level <= self.max_level

    def join(self, player: Player):
        self.players.append(player)

    def is_full(self, ) -> bool:
        return len(self.players) == self.capacity

    def get_infotext(self, ) -> str:
        info = []
        if self.is_full():
            info.append('Started!')
        else:
            info.append('Waiting!')
            
        for player in sorted(self.players):
            info.append(f'{player.level} {player.nickname}')

        return '\n'.join(info)

def simulate(capacity: int, players: List[Player]) -> List[Room]:
    all_rooms = []
    waiting_rooms = []

    for player in players:
        for i, room in enumerate(waiting_rooms):
            if room.is_joinable(player):
                room.join(player)
                if room.is_full():
                    waiting_rooms.pop(i)
                break
        else:
            new_room = Room(player, capacity)
            all_rooms.append(new_room)
            waiting_rooms.append(new_room)

    return all_rooms

pnum, capacity = map(int, stdin.readline().rstrip().split())
players = []
for _ in range(pnum):
    level, nickname = stdin.readline().rstrip().split()
    player = Player(nickname, int(level))
    players.append(player)

rooms = simulate(capacity, players)
for room in rooms:
    stdout.write(room.get_infotext())
    stdout.write('\n')