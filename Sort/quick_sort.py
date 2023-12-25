def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:

        # 왼쪽이 피봇보다 작은거
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        # 오른쪽이 피봇보다 큰거
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

        quick_sort(arr, start, right - 1)
        quick_sort(arr, right + 1, end)


arr = [1, 2, 4, 3]
quick_sort(arr, 0, len(arr)-1)
print(arr)