def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    i=0
    while 5**i<=n:
        i=i+1

    count=0
    for t in range(1,i):
        count=count+(n//5**t)
        
def trailingZeroes(self,n):
    """
    :type n: int
    :rtype: int
    """
    if n<5:
        return 0

    return (n//5+ self.trailingZeroes(n//5))

def trailingZeroes(self,n):
    """
    :type n: int
    :rtype: int
    """
    result=0
    while n>4:
        result=result+n//5
        n=n//5
    
    return result