def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    ans = []
    stack = []

    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmpNode = stack.pop()
            ans.append(tmpNode.val)
            root = tmpNode.right

    return ans

