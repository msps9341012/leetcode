class Solution(object):
    def depth(self, root):
        if not root:
            return 0
        return 1 + self.depth(root.left)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        l_d = self.depth(root.left)
        r_d = self.depth(root.right)
        if l_d > r_d:
            return (2**r_d - 1) + self.countNodes(root.left) + 1
        else:
            return (2**l_d - 1) + self.countNodes(root.right) + 1