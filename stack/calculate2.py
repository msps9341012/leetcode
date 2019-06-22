def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    stack=[]
    num=0
    op=[1]
    s=s+'+'
    for i in s:
        if i.isdigit():
            num = 10*num + int(i)
        elif i in "+-*/":
            stack.append(num)
            num=0
            if op[-1]=='*':
                stack.append(stack.pop()*stack.pop())
                op.pop()
            if op[-1]=='/':
                x=stack.pop()
                stack.append(stack.pop()/x)
                op.pop()
            if i in "*/":
                op.append(i)
            else:
                stack.append(i)

    stack.pop()
    res=stack.pop(0)
    while stack:
        value=stack.pop(0)
        if value=="+":
            res=res+stack.pop(0)
        if value=="-":
            res=res-stack.pop(0)
    return res        


def calculate(s):
    s += '+0'
    stack, num, preOp = [], 0, "+"
    for i in range(len(s)):
        if s[i].isdigit(): num = num * 10 + int(s[i])
        elif not s[i].isspace():
            if   preOp == "-":  stack.append(-num)
            elif preOp == "+":  stack.append(num)
            elif preOp == "*":  stack.append(stack.pop() * num)
            else:               
                stack.append(int(stack.pop() / num))
            preOp, num = s[i], 0
        print(stack)
    return sum(stack)
print(calculate("2*3*4"))

