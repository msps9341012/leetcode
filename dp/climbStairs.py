def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    res=[0]*(n+1)
    if n==0:
        return 1
    res[0]=1
    res[1]=1
    for i in range(2,n+1):
        res[i]=res[i-1]+res[i-2]
    return res[n]