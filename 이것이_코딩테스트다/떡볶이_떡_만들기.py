# 201 Page

n, m = map(int, input().split())
k = list(map(int, input().split()))

start = 1
end = max(k)  # 떡 중의 최대 길이

while start <= end:

    mid = (start + end) // 2
    total = 0

    for i in k:
        if i < mid:
            continue
        total += i - mid

    if total == m:
        print(mid)

    if total > m:
        start = mid + 1
    else:
        end = mid - 1
