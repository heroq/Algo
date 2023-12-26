
def binary_search(array, target, low, high):
    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid + 1

        elif array[mid] > target:
            high = mid - 1

        elif array[mid] < target:
            low = mid + 1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(array, 4, 0, len(array)-1))
