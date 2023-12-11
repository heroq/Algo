# 진행 필요

nums = [-1, 0, 1, 2, -1, -4]


# 1. 투 포인터를 사용한다.
# 2. 중복 된 값을 넘겨야한다.
# 3.

def threeSum(nums):
    nums.sort()  # 투 포인터 사용하니깐 정렬

    for i in range(len(nums) - 2):  # 3개 초과 할 때 시작
        if i > 0 and nums[i] == nums[i - 1]:  # 중복체크
            continue

        left, right = i + 1, len(nums) - 1  # 투 포인터 초기화

        while left < right: # right


