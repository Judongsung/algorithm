from sys import stdin
from math import ceil

n = int(stdin.readline())
roads = list(map(int, stdin.readline().split()))
prices = list(map(int, stdin.readline().split()))

cur_city = 0
used_money = 0
while cur_city < n-1:
    city_pass_through = 1
    cur_oil_price = prices[cur_city]
    while cur_city+city_pass_through < n and cur_oil_price < prices[cur_city+city_pass_through]:
        city_pass_through += 1
    
    charge_amount = sum(roads[cur_city:cur_city+city_pass_through])
    used_money += cur_oil_price*charge_amount
    cur_city += city_pass_through
    
print(used_money)