def rangeBitwiseAnd(self, m,n) :
    if m==0: return 0
    if int(math.log(m, 2)) != int(math.log(n, 2)) : return 0
    
    res = m
    for i in range(m+1, n+1):
        res = res&i
    return res

def rangeBitwiseAnd(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    p = 0
    while m != n:
        m >>= 1
        n >>= 1
        p += 1
    return m << p