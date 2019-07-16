def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    flag=1
    if x<0:
        flag=-1
        x=-1*x
    final=0
    while x!=0:
        final=final*10+x%10
        x=x//10
    final=flag*final
    print(final)

reverse(210)