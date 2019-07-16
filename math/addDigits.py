def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    while num//10!=0:
        s=str(num)
        num=0
        for i in s:
            num=num+int(i)
    return num
print(addDigits(38))