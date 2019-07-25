def checkp(s):
	if len(s)%2==0:
		return s[:len(s)//2]==s[len(s)//2:][::-1]
	else:
		return s[:len(s)//2]==s[len(s)//2+1:][::-1]

def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]

print(helper('abba',1,2))
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    res=""
    for i in range(len(s)):
    	for j in range(len(s),i,-1):
    		if len(s[i:j])<len(res):
    			break
    		if checkp(s[i:j]):
    			if len(s[i:j])>len(res):
    				res=s[i:j]
    			break
    	if len(s)==len(res):
    		break
    return res

print(longestPalindrome(""))
    