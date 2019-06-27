def isBalanced(self, root):
    if self.checkHeight(root) == -1:  
        return False
    else:  
        return True

def checkHeight(self, root):
    if root == None:  
        return 0
    leftHeight = self.checkHeight(root.left)
    if leftHeight == -1:
        return -1
    rightHeight = self.checkHeight(root.right)
    if rightHeight == -1:
        return -1
    diffHeight = abs(leftHeight - rightHeight)
    if diffHeight > 1:
        return -1
    else:
        return max(leftHeight, rightHeight) + 1


def isBalanced(self, root):
    stack = [(0, root)]
    depth = {None: 0}
    while stack:
        seen, node = stack.pop()
        if node is None:
            continue
        if not seen:
            stack.extend([(1, node), (0, node.right), (0, node.left)])
        else:
            if abs(depth[node.left] - depth[node.right]) > 1:
                return False
            depth[node] = max(depth[node.left], depth[node.right]) + 1
    return True
