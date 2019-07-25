#def generateParenthesis(n):

a=[]
def recur(string,stack,n):
	print(string,stack,n)
	if n==0 and not stack:
		a.append(string)
	if n>0:
		recur(string+'(',stack+['('],n-1)
	if stack:
		stack.pop()
		recur(string+')',stack,n)

def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    ans = []
    
    def _generate(cur, left, right):
        if left > right:
            return
        if left == 0 and right == 0:
            ans.append(cur)
            return
        
        if left > 0:
            _generate(cur + '(', left - 1, right)
        
        if right > 0:
            _generate(cur + ')', left, right - 1)
    
    _generate('', n, n)
    return ans

def generateParenthesis(self, n):
    res = []
    self.dfs(n, n, "", res)
    return res

def dfs(self, leftRemain, rightRemain, path, res):
    if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
        return  # backtracking
    if leftRemain == 0 and rightRemain == 0:
        res.append(path)
        return 
    self.dfs(leftRemain-1, rightRemain, path+"(", res)
    self.dfs(leftRemain, rightRemain-1, path+")", res)

