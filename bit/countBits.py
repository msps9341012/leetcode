
'''
n&(n-1)作用：将n的二进制表示中的最低位为1的改为0
'''
def countBits(self, num):
    """
    :type num: int
    :rtype: List[int]
    """
    res=[0]*(num+1)
    for i in range(1,num+1):
        res[i]=res[i&i-1]+1
    return res

res = [0]
while len(res) <= 4:
    res += [i+1 for i in res]
    print(res)
