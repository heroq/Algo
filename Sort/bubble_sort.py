# 옆에 있는 값 끼리 계속 비교하면서
# 큰 값을 뒤로 보낸다 (오름차순)
def bubble_sort(ary):
    # 마지막은 마지막전이랑 비교 하기에 빼준다.
    ary_max = len(ary) - 1

    for i in range(ary_max):

        # 버블정렬 후 i 만큼 뺀다, 뒤에는 정렬이 된 값이 있기때문
        cnt = ary_max - i
        for y in range(cnt):
            # y, y+1이면은 밑에 처럼 작동된다.
            # 0 1
            # 1 2
            # 2 3
            # 3 4
            if ary[y] > ary[y + 1]:
                ary[y], ary[y + 1] = ary[y + 1], ary[y]

    return ary


print(bubble_sort([5, 4, 3, 2, 1]))
