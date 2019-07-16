def reverseBits(n):
    x=bin(n)
    x='0b'+x[2:][::-1]
    return int(x,2)<<32-len(x)+2

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        shift = 31
        ans = 0
        while shift >= 0:
            ans += (n & 1) << shift #利用次方一直疊
            n >>= 1
            shift -= 1
        return ans
