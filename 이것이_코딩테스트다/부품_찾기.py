# 197 Page
import sys


def component_search(array, target_array, low, high):
    result = []

    for target in target_array:
        find_check = False
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = (low + high) // 2  # 중간 값 초기화
            if array[mid] == target:
                find_check = True
                break

            elif array[mid] > target:
                high = mid - 1

            elif array[mid] < target:
                low = mid + 1

        if find_check:
            result.append("yes")
        else:
            result.append("no")

    print(' '.join(result))


have_count = sys.stdin.readline().strip()  # 가지고 있는 부품 개수
have_array = list(set(map(int, sys.stdin.readline().strip().split())))  # 부품
have_array.sort()

find_count = sys.stdin.readline().strip()  # 찾는 부품 개수
find_array = list(map(int, sys.stdin.readline().strip().split()))  # 찾는 부품
find_array.sort()

component_search(have_array, find_array, 0, len(have_array) - 1)