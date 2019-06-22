def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    
    if root==None:
        return True
    p=root.left
    q=root.right
    stack=[(p,q)]
    while stack:
        p,q=stack.pop()
        if p and q:
            if p.val==q.val:
                stack.append((p.right,q.left))
                stack.append((p.left,q.right))
            else:
                return False
        elif p is not q:
            return False
    return True


def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root==None:
        return True
    p=root.left
    q=root.right

    return self.checksame(p,q)
       
    
def checksame(self,p,q):
    res=False
    if p==None and q==None:
        return True
    elif p and q:
        if p.val==q.val:
            if self.checksame(p.left,q.right):
                res=self.checksame(p.right,q.left)
            
    return res

def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def sym_tree(L,R):
        if L and R: 
            return L.val == R.val and sym_tree(L.left, R.right) and sym_tree(L.right, R.left)
        else:
            return L == R
    return sym_tree(root, root)
                    