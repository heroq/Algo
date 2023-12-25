# 출처 : leetcode 솔루션
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr, itr = [], head

        # itr에 head를 바라보게 한 후 arr에 값을 담는다.
        while itr:
            arr.append(itr.val)
            itr = itr.next
        arr.sort()

        # 다시 itr을 head를 바라보게 한다.
        itr, i = head, 0

        # 정렬 된 어레이값을 넣는다.
        while itr:
            itr.val = arr[i]
            i += 1
            itr = itr.next
        return head
