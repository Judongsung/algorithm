from typing import List, Union


class Video:
    def __init__(self, video_len: Union[str, int], op_start: Union[str, int], op_end: Union[str, int]):
        self.video_len = time_to_num(video_len) if isinstance(video_len, str) else video_len
        self.op_start = time_to_num(op_start) if isinstance(op_start, str) else op_start
        self.op_end = time_to_num(op_end) if isinstance(op_end, str) else op_end
    
    def is_op_section(self, num: int) -> bool:
        return self.op_start <= num <= self.op_end
    
    def move_pos(self, pos: int, move: int=0) -> int:
        pos += move
        if pos < 0:
            pos = 0
        elif pos > self.video_len:
            pos = self.video_len
            
        if self.is_op_section(pos):
            pos = self.op_end
        return pos

def time_to_num(time: str) -> int:
    mm, ss = time.split(":")
    return int(mm)*60+int(ss)

def num_to_time(num: int) -> str:
    mm, ss = divmod(num, 60)
    return str(mm).zfill(2)+":"+str(ss).zfill(2)

MOVE_TIME = 10
PREV = "prev"
NEXT = "next"
CMD_MOVES = {PREV: -10, NEXT: 10}

def solution(video_len: str, pos: str, op_start: str, op_end: str, commands: List[str]) -> int:
    video = Video(video_len, op_start, op_end)
    pos_num = time_to_num(pos)
    pos_num = video.move_pos(pos_num)
    
    for cmd in commands:
        pos_num = video.move_pos(pos_num, CMD_MOVES[cmd])
    
    return num_to_time(pos_num)