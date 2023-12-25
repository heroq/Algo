
def insertion_sort(arr):

    # 최대 값
    max_arr = len(arr)-1

    # 배열 전체를 조회
    # 0번쨰는 이미 정렬 된 것
    for i in range(1, max_arr):
        # i의 뒤에 있는 값을 조회
        for y in range(i+1, max_arr):

            tmp = max_arr - y
