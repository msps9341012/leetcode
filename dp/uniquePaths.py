
def uniquePaths(m, n,count):
	if m==0 and n==0:
		count.append(1)
	if m>0:
		uniquePaths(m-1,n,count)
	if n>0:
		uniquePaths(m,n-1,count)
def t():
	count=[]
	uniquePaths(23-1,12-1,count)
	print(sum(count))
t()