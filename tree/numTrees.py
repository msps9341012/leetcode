'''
概念為1-n 有n個node可以當root
n=3:
選1=number(0)*number(2) (左邊沒有)
通式為i=i-1*n-i
'''
def numTrees(self, n):
    res = [0] * (n+1)
    res[0] = 1
    for i in xrange(1, n+1):
        for j in xrange(i):
            res[i] += res[j] * res[i-1-j] #這邊的i 代表該round的n
    return res[n]

