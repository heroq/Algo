# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # 싱글 링크드 리스트 정렬.
        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next
        lst.sort()

        result = ListNode()
        node = ListNode()
        result.next = node

        for i in lst:
            node.val = i

            if i != lst[-1]:
                new_node = ListNode()
                node.next = new_node
                node = node.next

        return result.next
