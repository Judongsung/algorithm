from sys import stdin


MALE = 1
FEMALE = 2
ON = 1
OFF = 0

class SwitchManager:
    def __init__(self, switches: list):
        self.switches = switches

    def switch_one(self, num):
        if self.switches[num] == ON:
            self.switches[num] = OFF
        else:
            self.switches[num] = ON
    
    def switch_male(self, num: int):
        for i in range(num, len(self.switches)+1, num):
            idx = i-1
            self.switch_one(idx)

    def switch_female(self, num: int):
        num -= 1
        i = 1
        self.switch_one(num)
        while 0 <= num-i and num+i < len(self.switches) and self.switches[num-i] == self.switches[num+i]:
            self.switch_one(num-i)
            self.switch_one(num+i)
            i += 1

    def get_switches(self, ) -> list:
        return self.switches
    
n = int(stdin.readline())
switches = SwitchManager(list(map(int, stdin.readline().rstrip().split())))
students = int(stdin.readline())
for _ in range(students):
    gender, num = map(int, stdin.readline().rstrip().split())
    if gender == MALE:
        switches.switch_male(num)
    else:
        switches.switch_female(num)

result = switches.get_switches()
for i in range(0, len(result), 20):
    print(*result[i:i+20])