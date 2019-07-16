def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n==0:
        return False

    while n:
        if n==1:
            return True
        if n&1:
            return False
        n=n>>1
    return True

print(isPowerOfTwo(-2))