import bisect
import sys

have_count = sys.stdin.readline().strip()  # 가지고 있는 부품 개수
have_array = list(set(map(int, sys.stdin.readline().strip().split())))  # 부품
have_array.sort()

find_count = sys.stdin.readline().strip()  # 찾는 부품 개수
find_array = list(map(int, sys.stdin.readline().strip().split()))  # 찾는 부품
find_array.sort()

result_print = []
for i in find_array:
    result = bisect.bisect_left(have_array, i)
    if i == have_array[result] and result < len(have_array):
        result_print.append("yes")
    else:
        result_print.append("no")

print(' '.join(result_print))