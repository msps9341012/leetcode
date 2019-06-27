def connect(self,root):
    tmp=root
    while root and root.left:
        next = root.left
        while root:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            root = root.next
        root = next
    return tmp



def connect(self, root):
    """
    :type root: Node
    :rtype: Node
    """

    if not root:
        return root
    q = [root]
    while q:
        if len(q)>0:
            for i in range(1,len(q)):
                q[i-1].next=q[i]
        new_q = []
        for node in q:
            if node.left:
                new_q.append(node.left)
            if node.right:
                new_q.append(node.right)
        q = new_q
    return root

def connect1(self, root):
    if root and root.left and root.right:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
 
# BFS       
def connect2(self, root):
    if not root:
        return 
    queue = [root]
    while queue:
        curr = queue.pop(0)
        if curr.left and curr.right:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            queue.append(curr.left)
            queue.append(curr.right)