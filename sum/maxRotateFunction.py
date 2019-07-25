def maxRotateFunction(A):
    """
    :type A: List[int]
    :rtype: int
    """
    if not A:
        return 0
    
    res=float("-inf")
    for i in range(len(A)):
        tmp=0
        for j in range(len(A)):
        	if i+j>len(A):
        		
            tmp=tmp+j*B[i+j]
        res=max(res,tmp)
    return res
A = [4,3,2,6]


print(maxRotateFunction(A))

