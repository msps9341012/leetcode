def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head==None:
        return None
    dummy=ListNode(0)
    dummy.next=head
    node=dummy
    while node.next and node.next.next:
        curr=node.next
        data=node.next.val
        while curr.next and data==curr.next.val:
            curr=curr.next
        if curr!=node.next:
            node.next=curr.next
        else:
            node=node.next
    return dummy.next





