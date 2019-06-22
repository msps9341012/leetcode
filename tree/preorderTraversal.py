def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root==None:
        return []
    tmp=[]
    self.preorder(root,tmp)
    return tmp

def preorder(self,root,tmp):
    if root!=None:
        tmp.append(root.val)
        self.preorder(root.left,tmp)
        self.preorder(root.right,tmp)

#iterative 利用stack存右邊第一個
def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    stack, ans =[root], []
    while stack:
        node = stack.pop(-1)
        while node:
            if node.right:
                stack.append(node.right)
            ans.append(node.val)
            node=node.left
    return ans

'''
搞清楚下一個進來(需pop掉)的是誰 放進stack順序
'''

def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None: return []
    results = []
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        results.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return results