def checkpal(s):
	i=0
	j=len(s)-1
	while i<j:
		if s[i]!=s[j]:
			return False
		else:
			i=i+1
			j=j-1
	return True


#def gensubstring(s):

res=[]
def dfs(s,path,res):
	if not s:
		res.append(path)
	for i in range(len(s)):
		if checkpal(s[:i+1]):
			dfs(s[i+1:],path+[s[:i+1]],res)
dfs("aabc",[],res)
print(res)