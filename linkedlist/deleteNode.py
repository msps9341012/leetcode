def deleteNode(self, node):
    """
    要刪除node時 如果沒辦法access前一個node
    可以copy下一個的value 再連到下下個
    """
    node.val=node.next.val
    node.next=node.next.next
        