def array_partition(arr):
    arr.sort()
    return sum(arr[::2])


print(array_partition([1, 3, 2, 4]))