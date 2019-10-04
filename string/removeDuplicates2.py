def removeDuplicates2(S):
    """
    :type S: str
    :rtype: str
    """
    stack=[]
    for i in S:
        if stack and i==stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return ''.join(stack)

def removeDuplicates2(S):
    res=[]
    for i in S:
        res=res+[i]
        if len(res)>1 and res[-1]==res[-2]:
            res=res[:len(res)-2]
    return ''.join(res)
print(removeDuplicates2('abbaca'))
