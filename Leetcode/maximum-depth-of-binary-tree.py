# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # root가 없으면 깊이는 0으로 처리
        if root is None:
            return 0

        # 큐 초기값을 root를 넣어줌
        queue = collections.deque([root])

        # 깊이를 확인할 변수
        depth = 0

        # 큐가 존재 하다면 반복
        while queue:

            # 깊이 더하기
            depth += 1

            # 현재 큐 길이 만큼 반복
            for _ in range(len(queue)):

                # 제일 앞에 있는 것을 뺀다.
                x = queue.popleft()

                # left가 존재 하면 추가
                # left부터 추가 하기에 순서는 BFS는 left부터 볼것임
                if x.left:
                    queue.append(x.left)

                # right가 존재 하면 추가
                if x.right:
                    queue.append(x.right)

        return depth
