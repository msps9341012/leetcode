def removeNthFromEnd(self, head, n):
        """
        須考慮[1], [1,2] 也就是刪除head的情況
        可用dummy 
        """
        if head.next==None and n==1:
            return None
        fast=head
        slow=head
        for i in range(n):
            fast=fast.next
        while fast:
            previous=slow
            fast=fast.next
            slow=slow.next
        if slow.next:
            slow.val=slow.next.val
            slow.next=slow.next.next
        else:
            previous.next=None
        return head

def removeNthFromEnd(self, head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    for _ in xrange(n):
        fast = fast.next
    while fast and fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next