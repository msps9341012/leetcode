class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[0]
        if n==0:
            return res
        for i in range(n):
            for j in res[::-1]:
                res.append(j+2**i)
        return res
 
    def grayCode(self, n):
        res = [0]
        for i in range(1, 2**n):
            res.append(res[-1] ^ (i & -i))
        return res