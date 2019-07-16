def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    l=['(', ')', '{', '}', '[',']']
    stack=[]
    if len(s)==1:
        return False
    for i in s:
        if i not in [')',']','}']:
            stack.append(i)
        else:
            if len(stack)==0:
                return False
            else:
                if i==')':
                    if stack.pop()!='(':
                        return False
                elif i==']':
                    if stack.pop()!='[':
                        return False
                elif i=='}':
                    if stack.pop()!='{':
                        return False
    
    return len(stack)==0