from __future__ import annotations
from sys import stdin, stdout


def maximize_profit(n: int, prices: list[int]) -> int:
    profit = 0
    max_price = prices[-1]

    for i in range(n-2, -1, -1):
        price = prices[i]
        if price > max_price:
            max_price = price
        else:
            profit += max_price-price

    return profit

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    prices = list(map(int, stdin.readline().rstrip().split()))
    stdout.write(str(maximize_profit(n, prices)))
    stdout.write('\n')