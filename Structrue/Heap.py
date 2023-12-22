# 최대 힙
class Heap:

    def __init__(self, nums=[]):
        self.nums = [None] + nums

    def heap_up_sort(self):
        # 현재 위치
        cur = len(self.nums) - 1
        # 부모노드 위치
        parent = cur // 2

        while parent > 0:
            # 현재값이 부모보다 클 경우, 스왑
            if self.nums[cur] > self.nums[parent]:
                self.nums[cur], self.nums[parent] = self.nums[parent], self.nums[cur]

            # 현재값을 부모로 올라감
            cur = parent

            # 부모노드 위치
            parent = cur // 2

    def heap_down_sort(self, cur):

        # 왼쪽이나 오른쪽이 더 클 경우 스왑.
        # 0번부터 내려가야함
        biggest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self.nums)-1 and self.nums[cur] < self.nums[left] and self.nums[left] > self.nums[right]:
            biggest = left

        if right <= len(self.nums)-1 and self.nums[cur] < self.nums[right] and self.nums[left] < self.nums[right]:
            biggest = right

        if biggest != cur:
            self.nums[cur], self.nums[biggest] = self.nums[biggest], self.nums[cur]
            self.heap_down_sort(biggest)

    def insert(self, n):
        self.nums.append(n)
        self.heap_up_sort()

    def remove(self):
        if not self.nums:
            return None

        root = self.nums[1]
        self.nums[1] = self.nums[-1]
        self.nums.pop()
        self.heap_down_sort(1)
        return root


# 세팅 된 최대힙 배열
test = Heap([8, 6, 3, 4, 1, 2])
test.insert(9)
test.insert(5)
test.insert(7)
test.remove()
test.remove()
print()
