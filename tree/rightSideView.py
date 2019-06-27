'''
就是每個level的最後一個
'''
def rightSideView(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res, stack = [], [(root, 0)]
    while stack:
        curr, level = stack.pop()
        if curr:
            if len(res) == level: 
            #先走右子樹 如果level一樣就加 因為每個level只能有一個

                res.append(curr.val)
            stack.append((curr.left, level+1))
            stack.append((curr.right, level+1))
    return res