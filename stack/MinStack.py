#!/usr/bin/python
# -*- coding: UTF-8 -*-
class MinStack(object):
    '''
    需要小心
    0,1,0 pop 
    ''' 
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1=[]
        self.s2=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)
        if len(self.s2)==0 or x<=self.s2[-1]: #所以要小於等於
            self.s2.append(x)

    def pop(self):
        """
        :rtype: None
        """
        value=self.s1.pop()
        if value==self.getMin():
            self.s2.pop()
        return value

    def top(self):
        """
        :rtype: int
        """
        return self.s1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.s2[-1]


class MinStack2:
    def __init__(self):
        self.data = [(None, float('inf'))]

    def push(self, x):
        self.data.append((x, min(x, self.data[-1][1])))

    def pop(self):
        if len(self.data) > 1: 
            return self.data.pop()[0]

    def top(self):
        return self.data[-1][0]

    def getMin(self):
        return self.data[-1][1]
        
