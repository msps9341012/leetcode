class Solution(object):
    def myPow(self, a, b):
        if b < 0 :
            return 1 / self.helper(a, -b)
        else:
            return self.helper(a, b)
    
    def helper(self, a, b):
        if b == 0: return 1
        half = self.helper(a, b // 2)
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a



def myPow(a, b):
    res=1
    if b<0:
        a=1.0/a
        b=abs(b)
    while b:
        count=1
        tmp=a
        while (count<<1)<b:
            tmp=tmp*tmp
            count=count<<1
        b=b-count
        res=res*tmp
    print(res)

def myPow2(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    pow = 1
    while n:
        if n & 1:
            pow *= x
        x *= x
        n >>= 1
    return pow
print(myPow2(2,10))
