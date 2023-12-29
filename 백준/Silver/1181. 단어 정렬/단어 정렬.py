import sys

readline = sys.stdin.readline

n = int(readline())
m = list(set(str(readline().strip()) for _ in range(n)))
m.sort(key=lambda x: (len(x), x))

for s in m:
    print(s)