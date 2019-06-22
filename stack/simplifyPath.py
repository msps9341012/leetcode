def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    a=[]
    top=None
    path=path.replace('/','  ').split(" ")
    for i in path:
    	if i=="":
    		if top!='/':
    			a.append('/')
    	elif i==".":
    		continue
    	elif i=="..":
    		if len(a)>2:
    			a.pop()
    			a.pop()
    	else:
    		a.append(i)
    	print(i,a)
    	top=a[-1]
    print(a)
    if len(a)>1 and a[-1]=="/":
    	return (''.join(a))[:-1]
    else:
    	return (''.join(a))



def simplifyPath2(path):
        """
        :type path: str
        :rtype: str
        """        
        # Splitting is O(n*m) - where m is the length of the character to split, here this is O(n)
        plist = path.split('/')
        stack = []
        for directory in plist:
            if directory == "." or not directory: #"" 會被略過
                continue
            # Need this condition nested for case of /../a
            elif directory == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(directory)
        return "/" + "/".join(stack) #join 是加在element的後面, 若只有一個則沒影響


def simplifyPath(self, path):
    stack = []
    for token in path.split('/'):
        if token in ('', '.'):
            pass
        elif token == '..':
            if stack: stack.pop()
        else:
            stack.append(token)
    return '/' + '/'.join(stack)

