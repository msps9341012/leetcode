def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return None
    root.left,root.right = root.right, root.left
    
    self.invertTree(root.left)
    self.invertTree(root.right)
    
    return root