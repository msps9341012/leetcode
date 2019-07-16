def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    if len(a)>len(b):
        b='0'*(len(a)-len(b))+b
    elif len(b)>len(a):
        a='0'*(len(b)-len(a))+a
    res=""
    carry=0
    for i,j in zip(a[::-1],b[::-1]):
        if int(i)^int(j):
            if carry:
                res='0'+res
                carry=1
            else:
                res='1'+res
        elif int(i)&int(j):
            if carry:
                res='1'+res
            else:
                res='0'+res
            carry=1
        else:
            res=str(carry)+res
            carry=0
    if carry:
        res='1'+res
    print(res)

class Solution(object):
    def addBinary(self, a, b):
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]


