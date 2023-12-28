# 떡볶이 문제랑 일치
import sys

tree_count, tree_length = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree)

while start <= end:

    mid = (start + end) // 2
    total = 0

    for cut in tree:
        if cut > mid:
            total += cut - mid

    if total >= tree_length:
        start = mid + 1
    else:
        end = mid - 1

print(start-1, end)