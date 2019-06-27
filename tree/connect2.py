'''
用一個dummy去記
tmp 則是下一個level的起點
curr去改node的next
'''
def connect(self, root):
    res=root
    while root:
        cur = tmp = Node(0)
        while root:
            if root.left:
                cur.next = root.left
                cur = root.left
            if root.right:
                cur.next = root.right
                cur = root.right
            root = root.next
        root = tmp.next
    return res