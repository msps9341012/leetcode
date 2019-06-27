'''
要往上傳值 只能兩支branch選一支
但ans 為global update 逐步測試兩個都加的情況

'''

def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.res= float("-inf")
    self.ms(root)
    return self.res
def ms(self,root):
    if root==None:
        return float("-inf")
    else:
        l=max(self.ms(root.left),0)
        r=max(self.ms(root.right),0)
        self.res=max(self.res,root.val+r+l)
        return root.val+max(l,r)