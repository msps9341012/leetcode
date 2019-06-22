#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
'''
TypeError: 'str' object does not support item assignment
string是一种不可变的数据类型
'''
def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    s=list(s)
    v='aeiouAEIOU'
    i=0
    j=len(s)-1
    while i<j:
        if s[i] in v and s[j] in v:
            tmp=s[j]
            s[j]=s[i]
            s[i]=tmp
            i=i+1
            j=j-1
        elif s[i] in v:
            j=j-1
        elif s[j] in v:
            i=i+1
        else:
            i=i+1
            j=j-1
    return ''.join(s)

print(reverseVowels("aA"))