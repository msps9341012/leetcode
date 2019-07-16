def findTheDifference(s, t):
    """
    要注意 a,aa
    """
    a={}
    for i in s:
        if i not in a:
            a[i]=1
        else:
            a[i]=a[i]+1
    for j in t:
        if j not in a:
            return j
        else:
            a[j]=a[j]-1
    for i in a:
        if a[i]>0 or a[i]<0:
            return i


'''
xor with same value gives 0
'''
def findTheDifference(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    x = 0
    for c in s+t:
        x ^= ord(c)
    return chr(x)