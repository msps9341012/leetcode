def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    stack=[]
    count=0
    for i in ops:
        if i.lstrip('-').isdigit():
            stack.append(int(i))
            count=count+int(i)
        elif i=='C':
            count=count-stack.pop()
        elif i=='D':
            n=2*stack[-1]
            count=count+n
            stack.append(n)
        else:
            t=stack[-1]+stack[-2]
            count=count+t
            stack.append(t)
    return count
            

print(calPoints(["5","-2","4","C","D","9","+","+"]))