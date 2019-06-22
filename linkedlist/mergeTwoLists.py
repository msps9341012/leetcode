def mergeTwoLists(self, l1, l2):
    """
    開一條新的記
    """
    head = temp =  ListNode(0)
    while l1 or l2:
        if l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next                
        elif l1:
            temp.next = l1
            l1 = l1.next
        elif l2:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    return head.next

def mergeTwoLists(self, a, b):
    if a and b:
        if a.val > b.val:
            a, b = b, a
        a.next = self.mergeTwoLists(a.next, b)
    return a or b