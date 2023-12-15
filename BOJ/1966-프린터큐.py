# 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다.

# 첫번째는 문서의 개수, 몇 번째로 인쇄되었는지, 맨 왼쪽은 0번째
# 두번째는 n개의 문서의 중요도
# - 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

# 값이 클 수록 중요도가 높음


# 첫번째는 문서의 개수, 몇 번째로 인쇄되었는지 궁금한 문서
# 1 0 0번째 인덱스
# 5
# 4 2 2번째 인덱스
# 1 2 3 4
# 6 0 0번째 인덱스
# 1 1 9 1 1 1
from collections import deque

test_case = 1  # 찾을려는 문서 총 개수

for _ in range(test_case):
    dq = deque()
    n, m = map(int, "6 0".split())  # 문서 개수, 찾을려는 인덱스
    index = list(map(int, "1 1 9 1 1 1".split()))  # 문서

    for i, rank in enumerate(index):  # index, value 반복
        dq.append((i, rank))  # dq에 [index, value] 추가

    # 왜 정렬하지 ?
    # 높은값을 뒤로 보내기 위해, 그래서 몇 번째에 인쇄되는지 앎
    index.sort()
    count = 0

    while dq:
        i, rank = dq.popleft()  # i에 인덱스, rank에 중요도를 담는다.

        if rank == index[-1]:
            index.pop()
            count += 1

            if i == m:
                print(count)
                break
        else:
            dq.append((i, rank))
