
class ListNode(object):
     def __init__(self, x,next):
         self.val = x
         self.next = next

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def sortedListToBST(head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    if head==None:
        return None
    def to_bst(start,end):
        if start and start!=end:
            i=start
            j=start.next
            while j!=end:
                print(i.val,j.val)
                if j.next==None or j.next==end:
                    break
                else:
                    j=j.next.next
                i=i.next
            node=TreeNode(i.val)
            node.left=to_bst(start,i)
            node.right=to_bst(i.next,end)
            return node
    return to_bst(head,None)

