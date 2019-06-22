#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
要注意 100leetcode這種
'''
def decodeString(s):
    """
    :type s: str
    :rtype: str
    """

    a=[]
    tmp=""
    for i in s:
    	if i.isdigit():
    		a.append(i)
    	elif i==']':
    		tmp=""
    		value=a.pop()
    		while value!='[':
    			tmp=value+tmp
    			value=a.pop()
    		print(tmp)
    		tmp=tmp*a.pop()
    		a.append(tmp)
    	elif i=='[':
    		value=a.pop()
    		tmp=""
    		while value.isdigit():
    			tmp=value+tmp
    			if len(a)==0:
    				break
    			else:
    				value=a.pop()
    		if not value.isdigit():
    			a.append(value)
    		a.append(int(tmp))
    		a.append('[')
    	else:
    		a.append(i)
    	print(a)
    return ''.join(a)

def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    Qnum = []
    QAph = []
    ret = ''
    curnum = ''
    for i in s:
        if i.isdigit():
            curnum += i
        elif i == '[':
            Qnum.append(int(curnum))
            QAph.append('')
            curnum = ''
        elif i.isalpha():
            if Qnum == []:
                ret += i
            else:
                QAph[-1] += i
        else:
            aa = Qnum[-1] * QAph[-1]
            Qnum.pop()
            QAph.pop()
            if len(Qnum) == 0:
                ret += aa
            else:
                QAph[-1] += aa

    	print(Qnum,QAph,ret)
    return ret

def decodeString(s):
    stack = []
    stack.append(["", 1])
    num = ""
    for ch in s:
        if ch.isdigit():
          num += ch
        elif ch == '[':
            stack.append(["", int(num)])
            num = ""
        elif ch == ']':
            st, k = stack.pop()
            stack[-1][0] += st*k
        else:
            stack[-1][0] += ch
    	print(stack)
    return stack[0][0]


print(decodeString("2[abc]3[cd]ef"))

'''
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''