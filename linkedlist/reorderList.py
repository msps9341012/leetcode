from linkedlist import SingleLinkedList,ListNode
'''
def reorderList(head):
    
    if head==None:
        return None
    length=0
    node=head
    while node.next:
        node=node.next
        length=length+1
    fast=head
    slow=head
    dummy=ListNode(0)
    node=dummy
    while length>0:
        for i in range(length):
            fast=fast.next
        length=length-2
        next_node=slow.next
        slow.next=fast
        node.next=slow
        node=fast
        slow=fast=next_node
    if length<0:
        node.next=None
    else:
        node.next=slow
        node.next.next=None
    return dummy.next
'''

def reorderList(head):
    if not head: 
        return
    slow, fast = head, head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    #reverse
    previous=None
    tmp=slow.next
    slow.next=None
    while tmp:
        next=tmp.next
        tmp.next=previous
        previous=tmp
        tmp=next
    print(previous.data)
    node=head
    while node and previous:
        tmp=previous
        tmp2=node.next
        previous=previous.next
        tmp.next=node.next
        node.next=tmp
        node=tmp2



l=SingleLinkedList()
l.add_list_item(4)
l.add_list_item(3)
l.add_list_item(2)
l.add_list_item(1)

l.printall()
reorderList(l.root)
l.printall()

'''
r=reorderList(l.root)

tmp=""
node=r
while node is not None:
    tmp=tmp+str(node.data)+'->'
    node=node.next
print(tmp[:-2])
'''
