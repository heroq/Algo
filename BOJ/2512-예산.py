import sys

N = int(sys.stdin.readline())
K = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())


# 1 ~ 485.. ?


start = 1
end = max(K)

while start <= end:
    # 예산이 충분할경우
    if sum(K) < M:
        break

    mid = (start + end) // 2
