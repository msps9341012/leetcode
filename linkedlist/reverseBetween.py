from linkedlist import SingleLinkedList

def reverseBetween(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    last_previous=None
    previous=None
    i=1
    node=head
    if m==n:
        return head
    while node:
        tmp=node.next
        if m<=i<=n:
            if i==m:
                first=node
            if i==n:
                if last_previous:
                    last_previous.next=node
                first.next=tmp
            node.next=previous
            previous=node
            node=tmp
        else:
            if i==m-1:
                last_previous=node
            node=tmp
        i=i+1
    if m==1:
        return previous
    return head

l=SingleLinkedList()
l.add_list_item(5)
l.add_list_item(4)



l.printall()

x=reverseBetween(l.root,1,1)

tmp=""
while x is not None:
    tmp=tmp+str(x.data)+'->'
    x=x.next
print(tmp[:-2])
