from linkedlist import SingleLinkedList

def oddEvenList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head==None:
        return None
    if head.next==None:
        return head
    odd=head
    even=head.next
    tmp=even
    while odd or even:
        if odd.next!=None and odd.next.next!=None:
            odd.next=odd.next.next
            odd=odd.next
            if even.next.next:
                even.next=even.next.next
                even=even.next
        else:
            break
    odd.next=tmp
    even.next=None
    return head

def oddEvenList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head==None:
        return None

    odd=head
    even=head.next
    evenhead=even
    while even!=None and even.next!=None:
        odd.next=even.next
        odd=odd.next
        even.next=odd.next
        even=even.next
    odd.next=evenhead
    return head


