#def minCut(s):


def checkpal(s):
	return s==s[::-1]

#def gensubstring(s):
from collections import deque
def bfs(s):
	q=deque()
	visited=set()
	for i in range(1,len(s)):
		if s[:i] not in visited and checkpal(s[:i]):
			visited.add(s[:i])
			q.append((1,s[i:]))
	print(q)
	while q:
		step,left=q.popleft()
		if checkpal(left):
			return step
		else:
			for i in range(1,len(left)):
				if left[:i] not in visited and checkpal(left[:i]):
					visited.add(left[:i])
					q.append((step+1, left[i:]))
		print(q)


def minCut(s):
    n = len(s)
    dp = [0 for _ in xrange(n+1)]
    ispa = [False for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(i+1):
            if s[i] == s[j] and (i-j <= 1 or ispa[j+1]):
                ispa[j] = True
                if dp[i+1]:
                    dp[i+1] = min(dp[j] + 1, dp[i+1])
                else:
                    dp[i+1] = dp[j] + 1
            else:
                ispa[j] = False
            print(i,j,ispa,dp)
    return dp[n] - 1

print(minCut("abccba"))

