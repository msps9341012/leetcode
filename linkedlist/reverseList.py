def reverseList(self, head):
    node=head
    previous=None
    while node:
        tmp=node.next
        node.next=previous
        previous=node
        node=tmp
    return previous

def reverseList_recursive(head):
    if head is None or head.next is None:
        return head
 
    p=reverseList_recursive(head.next)
    head.next.next = head;
    head.next = None
    return p