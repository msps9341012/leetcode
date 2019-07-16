class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        res=[]
        def preorder(root,res):
            if root:
                res.append(root)
                preorder(root.left,res)
                preorder(root.right,res)
        
        preorder(root,res)
        for i in range(1,len(res)):
            res[i-1].right=res[i]
            res[i-1].left=None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        
        q = [root]
        par = None
        while q:
            node = q.pop()
            if node:
                q += [node.right, node.left]
                if par:
                    par.left = None
                    par.right = node
                par = node


    class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return
        l, r = root.left, root.right    
        root.left, root.right = None, l
        self.flatten(l)
        while root.right: root = root.right
        root.right = r
        self.flatten(r)