def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    stack = [(p, q)]
    while stack:
        n, m = stack.pop()
        if n and m:
            if n.val != m.val:
                return False
            stack.append((n.right, m.right))
            stack.append((n.left, m.left))
        elif n is not m:
            return False
    return True

## recursive
def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    res=False
    if p==None and q==None: 
        res=True
    elif p and q:
        if p.val==q.val:
            if self.isSameTree(p.left,q.left):
                res=self.isSameTree(p.right,q.right)
    return res