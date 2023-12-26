from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in range(len(matrix)):
            print(x)
            for y in range(len(matrix[x])):
                print(x, y)
                if target == matrix[x][y]:
                    return True

        return False