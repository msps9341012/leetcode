def binaryTreePaths(self, root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if root==None:
        return None

    string=""
    res=[]
    def printorder(root,string,res):
        if root:
            if not root.left and not root.right:
                res.append(string+str(root.val))
            else:
                string=string+str(root.val)+'->'
                printorder(root.left,string,res)
                printorder(root.right,string,res)
    printorder(root,string,res)
    return res

def binaryTreePaths(self, root):
    if not root:
        return []
    res, queue = [], [(root, "")]
    while queue:
        node, ls = queue.pop(0)
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.left:
            queue.append((node.left, ls+str(node.val)+"->"))
        if node.right:
            queue.append((node.right, ls+str(node.val)+"->"))
    return res


def binaryTreePaths(self, root):
    if not root:
        return []
    res, stack = [], [(root, "")]
    while stack:
        node, ls = stack.pop()
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.right:
            stack.append((node.right, ls+str(node.val)+"->"))
        if node.left:
            stack.append((node.left, ls+str(node.val)+"->"))
    return res

