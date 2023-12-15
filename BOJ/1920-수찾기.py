# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
import collections

# 여기서 4번째 줄이 2번째 줄에 포함되는지를 찾는 문제.

N = int(input())
first = list(map(int, input().split()))

M = int(input())
second = list(map(int, input().split()))


a = collections.Counter(first)

for i in second:
    if a[i] > 0:
        print(1)
    else:
        print(0)