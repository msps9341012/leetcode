def reverseString(self, s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    i=0
    j=len(s)-1
    while i<j:
        s[i],s[j]=s[j],s[i]
        i=i+1
        j=j-1


def recursive_reverse(s):
    if s == "":
        return s
    else:
        return rreverse(s[1:]) + s[0]