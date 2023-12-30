import collections
import sys

readline = sys.stdin.readline
n = int(readline())
check = [0] * 10001

for _ in range(n):
    check[int(readline())] += 1

for i in range(0, 10001):
    while check[i] > 0:
        sys.stdout.write(str(i)+"\n")
        check[i] -= 1


