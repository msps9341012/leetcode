from linkedlist import SingleLinkedList

def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if head==None:
        return None
    if head.next==None:
        return head

    #count length
    i=1
    tail=head
    while tail.next:
        tail=tail.next
        i=i+1
    if k%i==0:
        return head
    node=head
    for j in range(i-k%i-1):
        node=node.next
    new_head, tail.next, node.next=node.next,head,None
    return new_head




