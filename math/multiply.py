def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    
    s2=0
    for i in num2:
        s2=s2*10+int(i)
    order=0
    res=0
    num1=list(num1)
    while num1:
        n=num1.pop()
        res=res+int(n)*s2*(10**order)
        order=order+1
    return str(res)

print(multiply('3','2'))