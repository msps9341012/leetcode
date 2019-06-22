def swapPairs(head):
    index=0
    node=head
    last_previous=None
    head_node=head
    while node:
        index=index+1
        tmp=node.next
        if index%2==0:
            previous.next=tmp
            node.next=previous
            if last_previous:
                last_previous.next=node
            last_previous=previous
        if index==2:
            head_node=node
        previous=node
        node=tmp
    return head_node



def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next