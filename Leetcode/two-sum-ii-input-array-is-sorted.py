# 출처 : 리트코드 솔루션
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i <= j:
            s = numbers[i] + numbers[j]

            if s == target:
                return [i+1, j+1]

            if s > target:
                j -= 1
            else:
                i += 1


test = Solution()
print(test.twoSum([-1,0], -1))
