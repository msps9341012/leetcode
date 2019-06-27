def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root==None:
        return 0
    l=self.maxDepth(root.left)
    r=self.maxDepth(root.right)
    return max(l,r)+1