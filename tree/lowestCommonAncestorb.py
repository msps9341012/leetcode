class TreeNode(object):
     def __init__(self, x,left,right):
         self.val = x
         self.left = left
         self.right = right


x=TreeNode(3,TreeNode(5,TreeNode(6,None,None),TreeNode(2,TreeNode(7,None,None),TreeNode(4,None,None))),TreeNode(1,TreeNode(0,None,None),TreeNode(8,None,None)))


def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    dict_node={p:[],q:[]}
    stack=[(root,[])]
    while stack:
        node,previous=stack.pop()
        if node.right:
            stack.append((node.right,previous+[node.val]))
        if node.left:
            stack.append((node.left,previous+[node.val]))
        if node.val in dict_node:
            dict_node[node.val]=dict_node[node.val]+previous+[node.val]

    print(dict_node[p],dict_node[q])
    for i in dict_node[p][::-1]:
        if i in dict_node[q]:
            return(i)


def lowestCommonAncestor(root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()
            
            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q

print(lowestCommonAncestor(x,6,4))