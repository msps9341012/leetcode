
def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    p_val = p.val

    q_val = q.val

    node = root

    while node:

        parent_val = node.val

        if p_val > parent_val and q_val > parent_val:    
            # If both p and q are greater than parent
            node = node.right
        elif p_val < parent_val and q_val < parent_val:
            # If both p and q are lesser than parent
            node = node.left
        else:
            # We have found the split point, i.e. the LCA node.
            return node