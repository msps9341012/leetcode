def isPalindrome(self, head):
    if not head:
        return True
    fast = slow = head
    prev = None
    #只reverse到中間
    while fast.next and fast.next.next:
        fast = fast.next.next
        nn = slow.next
        slow.next = prev
        prev = slow
        slow = nn
    # 偶數
    if fast.next:
        nn = slow.next
        slow.next = prev
        prev = slow
        slow = nn
    # 基數
    else:
        slow = slow.next
    
    while slow:
        if slow.val != prev.val:
            return False
        slow = slow.next
        prev = prev.next
    return True