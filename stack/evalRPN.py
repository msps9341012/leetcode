import math
def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    a=[]
    operators=['+','-','*','/']
    for i in tokens:
        if i not in operators:
            a.append(int(i))
        else:
            x1=a.pop()
            x2=a.pop()
            if i=='+':
                a.append(x2+x1)
            elif i=='-':
                a.append(x2-x1)
            elif i=="*":
                a.append(x2*x1)
            elif i=='/':
                a.append(int(float(x2)/x1)) # for the case: 6/-132, should return 0
        print(a)
    return a.pop()


def recursive_evalRPN(self, tokens: List[str]) -> int:
    t, f = tokens.pop(), self.evalRPN
    if t in '+-*/':
        b, a = f(tokens), f(tokens)
        t = eval('a' + t + 'b')
    return int(t)    
tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

evalRPN(tokens)
    