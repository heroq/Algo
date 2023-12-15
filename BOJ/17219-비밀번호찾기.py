import collections

N, M = list(map(int, input().split()))
table = collections.defaultdict()

for i in range(N):
    addr, pw = list(map(str, input().split()))
    table[addr] = pw

for i in range(M):
    print(table[input()])