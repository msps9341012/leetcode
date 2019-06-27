#Pre-order is one type of DFS.


 class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return ''
            res = [str(node.val)]
            res.append(dfs(node.left))
            res.append(dfs(node.right))
            return ','.join(res)
        
        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(nodes, index):
            if index >= len(nodes) or nodes[index] == None:
                return None, index
            node = TreeNode(nodes[index])
            node.left, index = dfs(nodes, index + 1)
            node.right, index = dfs(nodes, index + 1)
            return node, index
        
        nodes = list(map(lambda x: None if not x else int(x), data.split(',')))
        return dfs(nodes, 0)[0]


class Codec:
    def serialize(self, root):    
        if not root: return ""
        q = collections.deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            res.append(str(node.val) if node else '#')
        return ','.join(res)
                
    '''
    用一個queue去接上一個
    '''
    def deserialize (self, data):
        if not data: return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = collections.deque([root])
        index = 1
        while q:
            node = q.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1
        
            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
        return root