import itertools
import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
black_jack = -1

a = itertools.combinations(card, 3)
for i in a:
    if black_jack < sum(i) <= m:
        black_jack = sum(i)

print(black_jack)