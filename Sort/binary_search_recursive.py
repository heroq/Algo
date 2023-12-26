
def binary_search(array, target, low, high):
    if low >= high:
        return None

    # 중간 위치 확인
    mid = (low + high) // 2

    # 값이 일치 하면 반환
    if array[mid] == target:
        return mid + 1

    # 타겟이 작을경우 왼쪽
    elif array[mid] > target:
        binary_search(array, target, low, mid - 1)

    # 타겟이 클경우 오른쪽
    elif array[mid] < target:
        binary_search(array, target, mid + 1, high)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(array, 5, 0, len(array)))