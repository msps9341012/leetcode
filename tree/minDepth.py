'''
BFS 可以找shortest path
'''

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

'''
檢查左右子樹
when min(l, r) is 0, which means the leftchild or rightchild of node is not exist, 
then return the max(l, r) which is length of another branch.
'''

def minDepth(self, root):
    if not root: return 0
    l = self.minDepth(root.left)
    r = self.minDepth(root.right)
    return (min(l, r) or max(l, r)) +1