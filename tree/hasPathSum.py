def hasPathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if not root:
        return False
    res, stack = [], [(root, 0)]
    while stack:
        node, ls = stack.pop()
        if not node.left and not node.right:
            if (ls+node.val)==sum:
                return True
        if node.right:
            stack.append((node.right, ls+node.val))
        if node.left:
            stack.append((node.left, ls+node.val))
    return False