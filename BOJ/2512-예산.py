# 출처 : https://great-park.tistory.com/44

import sys

N = int(sys.stdin.readline())
K = list(map(int, sys.stdin.readline().split()))
K.sort()
M = int(sys.stdin.readline())

start = 1
end = max(K)

while start <= end:
    mid = (start + end) // 2
    amount = 0

    for x in K:
        if x <= mid:
            amount += x
        else:
            amount += mid

    if amount > M:
        end = mid - 1
    else:
        start = mid + 1

print(end)
