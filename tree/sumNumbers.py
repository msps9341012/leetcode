def sumNumbers(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    res=0
    stack=[(root,0)]
    while stack:
        node,tmp=stack.pop()
        if not node.left and not node.right:
            tmp=10*tmp+node.val
            res=res+tmp
        if node.right:
            stack.append((node.right,10*tmp+node.val))
        if node.left:
            stack.append((node.left,10*tmp+node.val))
    return res

def sumNumbers(self, root):
    if root is None:
        return 0
    
    def sumpath(root,count):
        if root is None:
            return 0
        count = 10*count + root.val
        if root.left is None and root.right is None: 
            return count
        return sumpath(root.left,count)+sumpath(root.right,count)
    
    return sumpath(root,0)