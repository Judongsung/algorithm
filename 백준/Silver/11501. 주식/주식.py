from __future__ import annotations
from sys import stdin, stdout


def maximize_profit(prices: list[int]) -> int:
    profit = 0
    max_price = prices[-1]

    for price in reversed(prices[:-1]):
        if price > max_price:
            max_price = price
        elif price < max_price:
            profit += max_price-price

    return profit

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    prices = list(map(int, stdin.readline().rstrip().split()))
    stdout.write(str(maximize_profit(prices)))
    stdout.write('\n')