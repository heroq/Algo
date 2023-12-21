def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    def mergeNode(t1, t2):
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = mergeNode(t1.left, t2.left)
            node.right = mergeNode(t1.right, t2.right)
            return node
        else:
            return t1 or t2

    return mergeNode(root1, root2)