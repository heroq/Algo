
nums = [-1, 0, 1, 2, -1, -4]


# 1. 투 포인터를 사용한다.
# 2. 중복 된 값 확인

def threeSum(nums):
    result = []
    nums.sort()  # 투 포인터 사용하니깐 정렬

    for i in range(len(nums) - 2):  # 3개 초과 할 때 시작
        if i > 0 and nums[i] == nums[i - 1]:  # 중복체크
            continue

        left, right = i + 1, len(nums) - 1  # 투 포인터 초기화

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:  # 정렬을 했기에 값이 크면 left를 올려서 맞춰준다.
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1

                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1

    return result


print(threeSum(nums))