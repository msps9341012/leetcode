'''
a.append() 不會回傳
a+[] 才會
'''
def pathSum(self,root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    if not root:
        return []
    res = []
    self.dfs(root, sum, [], res)
    return res

def dfs(self, root, sum, ls, res):
    if not root.left and not root.right and sum == root.val:
        ls.append(root.val)
        res.append(ls)
    if root.left:
        self.dfs(root.left, sum-root.val, ls+[root.val], res)
    if root.right:
        self.dfs(root.right, sum-root.val, ls+[root.val], res)



def pathSum(root, sum2):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    if not root:
        return []
    res, stack = [], [(root, [])]
    while stack:
        node,route = stack.pop()

        if not node.left and not node.right:
            route.append(node.val)

            if sum(route)==sum2:
                res.append(route)
        if node.right:
            stack.append((node.right,route+[node.val]))
        if node.left:
            stack.append((node.left,route+[node.val]))
    return res


print(pathSum(x,22))