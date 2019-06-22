def hasCycle(self, head):
    seen={}
    while head:
        if head in seen: #head=node object 屬性可以放入dict（記憶體位置會不同）
            return True
        else:
            seen[head]=True
        head=head.next
    return False

def hasCycle_two_pointer(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head==None or head.next==None:
        return False
    fast=head.next
    slow=head
    while slow!=fast:
        if fast is None or fast.next is None:
            return False
        else:
            slow=slow.next
            fast=fast.next.next
    return True
def hasCycle(self, head):
    """
    將測過的都指回head 若有cycle也會指到head
    """
    node=head
    while node and node.next!=head:
        tmp=node.next
        node.next=head
        node=tmp
    return node!=None


def hasCycle(self, head):
    """
    reverse list 若有cycle 則回接回head
    因有設previous=None 所以可以跳出while loop
    """
    if not (head and head.next):
        return False
    
    reversed_head = self.reverseList(head)
    return reversed_head is head
    
def reverseList(self, head):
    prev_node = None
    while head:
        next_node = head.next
        head.next = prev_node
        prev_node = head
        head = next_node
        
    return prev_node