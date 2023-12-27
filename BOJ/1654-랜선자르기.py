import sys

# 4개의 랜선이 있고 11개를 만들어야한다.

K, N = map(int, sys.stdin.readline().split())
lan_list = list(int(sys.stdin.readline()) for _ in range(K))

start = 1
end = max(lan_list)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in lan_list:
        # start가 0이면 0을 나눠서 오류가 생기는 현상이 있었음
        total += i // mid

    # 랜선이 많으면
    if total >= N:
        # 제일 큰 값을 저장
        result = mid
        start = mid + 1

    # 랜선이 적으면
    else:
        end = mid - 1

print(result)