def singleNumber(nums):
    bit = [0] * 32
    for num in nums:
        for i in xrange(32):
            bit[i] += num >> i & 1
    res = 0
    print(bit)
    for i, val in enumerate(bit):
        # if the single numble is negative,
        # this case should be considered separately 
        if i == 31 and val%3:
            res = -((1<<31)-res)
        else:
            res |= (val%3)*(1<<i)
        print(res)
    return res

def singleNumber(self, nums):
    a = b = 0
    for n in nums:
        b = (b^n)&~a
        a = (a^n)&~b
    return b


class Solution:
# @param A, a list of integer
# @return an integer
def singleNumber(self, A):
    ans = 0
    for i in xrange(0,32):
        count = 0
        for a in A:
            if ((a >> i) & 1):
                count+=1
        ans |= ((count%3) << i)
    return self.convert(ans)
    
def convert(self,x):
    if x >= 2**31:
        x -= 2**32
    return x