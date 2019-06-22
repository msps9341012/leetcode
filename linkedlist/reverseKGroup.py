from linkedlist import SingleLinkedList, ListNode

def reverseKGroup(head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        i=1
        node=head
        while node:
            next_node=node.next
            print(i,node.data)
            if i==k:
                new_head, tail_node=reverse(head,k)
                p.next=new_head
                p=tail_node
                tail_node.next=next_node
                head=next_node
                i=0
            node=next_node
            i=i+1
        return dummy.next
    
def reverse(node,k):
    tmp=node
    previous=None
    while tmp:
        tmp.next, previous, tmp =previous, tmp, tmp.next
        k=k-1
        if k==0:
            return previous,node

l=SingleLinkedList()
l.add_list_item(2)
l.add_list_item(1)


l.printall()


r=reverseKGroup(l.root,2)
tmp=""
while r is not None:
    tmp=tmp+str(r.data)+'->'
    r=r.next
print(tmp[:-2])

