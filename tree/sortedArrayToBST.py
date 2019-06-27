class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    def to_bst(start,end):
        if start>end:
            return None
        mid=(start+end)//2
        node=TreeNode(nums[mid])
        node.left=to_bst(start,mid-1)
        node.right=to_bst(mid+1,end)
        return node
    return to_bst(0,len(nums)-1)

def sortedArrayToBST2(nums):
    def helper(nums, l, r):
        if l <= r:
            mid = l + (r-l)//2
            
            root = TreeNode(nums[mid])
            root.left = helper(nums, l, mid-1)
            root.right = helper(nums, mid+1, r )
            return root

    return helper(nums, 0, len(nums)-1)



x=[-10,-3,0,5,9]
node=sortedArrayToBST2(x)
print(node.val)
print(node.left.val)
print(node.right.val)