'''
要注意[2,3,1]這種
BST 用inorder應該是要遞增 用這個去解
'''

def recoverTree(self, root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    stack = []
    trav = root
    prev = None
    left = None
    right = None
    while stack or trav:
        if trav:
            stack.append(trav)
            trav = trav.left
        else:
            u = stack.pop()
            if prev and prev.val > u.val:
                if not left:
                    left = prev
                    curr = u
                else:
                    right = u
            prev = u
            trav = u.right
    if right:
        left.val, right.val = right.val, left.val
    else:
        left.val, curr.val = curr.val, left.val

