import heapq
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lst = heapq.nlargest(2, nums)
        return (lst[0]-1) * (lst[1]-1)
