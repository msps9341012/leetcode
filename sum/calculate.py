def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    num=[]
    operator="+-"
    tmp=""
    s=s[::-1]
    s=s+"+"
    for i in s:
        if i.isdigit():
            tmp=i+tmp
        elif i in operator:
            if len(tmp)>0:
                num.append(int(tmp))
                tmp=""
            num.append(i)
        elif i=="(":
            if len(tmp)>0:
                num.append(int(tmp))
                tmp=""
            value=num.pop()
            res=value
            while value!=')':
                if value=='+':
                    res=num.pop()+res
                elif value=="-":
                    res=res-num.pop()
                if len(num)>0:
                    value=num.pop()
                else:
                    break
            num.append(res)
        elif i==")":
            num.append(i)
        print(num)
    num.pop()
    result=value=num.pop()
    while num:
        if value=='+':
            result=result+num.pop()
        if value=="-":
            result=result-num.pop()
        if len(num)>0:
            value=num.pop()
        else:
            return result
    return result

print(calculate("2-(5-6)"))

'''
def calculate(s):
    numstack = []
    opstack = []
    i = len(s) -1
    while i > -1:
        if s[i] in '0123456789':
            j  = i
            while  i > -1 and s[i] in '0123456789':
                i -= 1
            i += 1
            numstack.append(int(s[i:j+1]))
        else:
            if s[i] in ')+-':
                opstack.append(s[i])
            if s[i] == '(':
                while opstack[-1] != ')':
                    if opstack.pop() == '+':
                        numstack.append(numstack.pop()+numstack.pop())
                    else:
                        numstack.append(numstack.pop()-numstack.pop())
                opstack.pop()
        i -= 1
        print(numstack)
    while opstack:
        if opstack.pop()=='+':
            numstack.append(numstack.pop()+numstack.pop())
        else:
            numstack.append(numstack.pop()-numstack.pop())
    return numstack[-1]
'''

'''
Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1+2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''