def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root==None:
        return 0
    stack=[(root,0)]
    min_length=float("inf")
    while stack:
        node,n=stack.pop()
        if node.left==None and node.right==None:
            n=n+1
            if n<min_length:
                min_length=n
        if node.right:
            stack.append((node.right,n+1))
        if node.left:
            stack.append((node.left,n+1))
    return min_length