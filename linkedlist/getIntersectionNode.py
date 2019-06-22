def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    dup_dict={}
    while headA:
        if headA not in dup_dict:
            dup_dict[headA]=True
        headA=headA.next

    while headB:
        if headB in dup_dict:
            return headB
        else:
            headB=headB.next
    return None

#抓出兩個list長度的差距
def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        A_pointer = headA
        B_pointer = headB
        while A_pointer != B_pointer:
            A_pointer = headB if A_pointer == None else A_pointer.next
            B_pointer = headA if B_pointer == None else B_pointer.next
        return A_pointer


def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a = len_b = 0
        p_a, p_b = headA, headB
        while p_a is not None or p_b is not None:
            if p_a is not None:
                p_a = p_a.next
                len_a += 1
            if p_b is not None:
                p_b = p_b.next
                len_b += 1
        diff = abs(len_a - len_b)
        if len_a > len_b:
            start, other_start = headA, headB
        else:
            start, other_start = headB, headA
        for _ in range(diff):
            start = start.next
        p1, p2 = start, other_start
        while True:
            if p1 == p2:
                return p1
            p1, p2 = p1.next, p2.next