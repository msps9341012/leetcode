def isValidBST(self, root):
    """
    不用全部走完 確認每一個新增的node即可
    """
    stack, inorder = [], float('-inf')
    
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        # If next element in inorder traversal
        # is smaller than the previous one
        # that's not BST.
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right

    return True


def isValidBST(self, root):
    """
    更新上下界的
    亦可用dfs iterative去解
    """
    def helper(node, lower = float('-inf'), upper = float('inf')):
        if not node:
            return True
        
        val = node.val
        if val <= lower or val >= upper:
            return False

        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True

    return helper(root)