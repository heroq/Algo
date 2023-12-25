# 제일 최솟값을 찾아서 위치를 변경 해준다.
def selection_sort(arr):
    max_arr = len(arr)

    # 배열의 전체를 조회
    for i in range(max_arr):

        # 최솟값 변수
        min_index = i

        # y는 이미 정렬 된 수를 제외 후 조회를 한다.
        for y in range(i + 1, max_arr):

            # 변수에 제일 값이 낮은 인덱스를 저장
            if arr[min_index] > arr[y]:
                min_index = y

        # 초기에 지정한 값이랑 다를경우, 변경사항이 있다면
        if min_index != i:
            # 스왑
            arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr


print(selection_sort([5, 4, 3, 2, 1]))
