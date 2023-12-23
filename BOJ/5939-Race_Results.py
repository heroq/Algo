import sys

length = int(sys.stdin.readline().strip())
lst = []

for i in range(length):
    h, m, s = map(int, sys.stdin.readline().strip().split())
    lst.append((h, m, s))

lst.sort()

for t in lst:
    print(' '.join(map(str, t)))
