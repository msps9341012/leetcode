def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    i=x//2
    while i*i>x:
        i=i-1
    return i

10//2 5

print(mySqrt())
