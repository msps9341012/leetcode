class TreeNode(object):
     def __init__(self, x,left,right):
         self.val = x
         self.left = left
         self.right = right

tree=TreeNode(1,TreeNode(7,TreeNode(7,None,None),TreeNode(-8,None,None)),TreeNode(0,None,None))


def maxLevelSum(root):
	res=[]
	stack=[(root,0)]
	depth=-1
	while stack:
		curr,level=stack.pop(0)
		if depth==level:
			res[level]=res[level]+curr.val
		else:
			res.append(curr.val)
			depth=level
		if curr.left:
			stack.append((curr.left,level+1))
		if curr.right:
			stack.append((curr.right,level+1))

	return res.index(max(res))+1

print(maxLevelSum([]))