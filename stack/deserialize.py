'''
要注意 [[]],[]
NestedInteger: https://my.oschina.net/yysue/blog/1829176
'''
def deserialize(self, s):
    if s[0]!='[':
        return NestedInteger(int(s))
    stack, num = [], ""
    for c in s:
        if c.isdigit() or c == "-": num += c
        elif c == "," and num:
            stack[-1].add(NestedInteger(int(num)))
            num = ""
        elif c == "[":
            elem = NestedInteger()
            stack.append(elem)
        elif c == "]":
            if num:
                stack[-1].add(NestedInteger(int(num)))
                num = ""
            x=stack.pop()
            if stack:
                stack[-1].add(x)
            else:
                return x
    return stack.pop()