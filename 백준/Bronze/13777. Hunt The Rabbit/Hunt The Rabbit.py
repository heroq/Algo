import bisect
import sys

# 1~50까지 순차적 번호가 매져긴 50개

# 항상 25를 첫 번째 봉투로 확인합니다.

# 0이면 종료.

# 짝수인 경우에는 두 개의 중간 봉투 중 낮은 번호의 봉투

# 출력

# 각 입력 줄에 대해 토끼 그림을 찾을 때까지 개봉한 모든 봉투의 번호를 개봉한 순서대로 출력합니다.
# 각 숫자는 이전 숫자와 공백으로 구분된 같은 줄에 있어야 합니다.

readline = sys.stdin.readline

# 50까지 세팅
numbers = [None] + [i for i in range(1, 51)]

while True:
    n = int(readline())
    if n == 0:
        break

    stack = []
    start = 1
    end = 50
    mid = 25

    if mid == n:
        print(25)

    while n != mid:
        mid = (start + end) // 2
        stack.append(mid)
        if n > mid:
            start = mid + 1
        else:
            end = mid - 1

    if stack:
        print(' '.join([str(num) for num in stack]))