def integerBreak(n):
    """
    :type n: int
    :rtype: int
    """
    if n==2:
    	return 1
    res=[1]*(n+1)
    for i in range(3,n+1):
    	tmp=0
    	for j in range(1,i//2+1):
    		left=j
    		right=i-j

    		tmp=max(tmp,max(res[left],left)*max(res[right],right))
    	res[i]=tmp
    return res[n]

def integerBreak(self,n):
    """
    :type n: int
    :rtype: int
    """
    if n==2:
        return 1
    if n==3:
        return 2
    product = 1;
    while n>4:
        product=product*3
        n=n-3
    
    product=product*n
    
    return product


def integerBreak(self,n):
    """
    用越多3越好
    """
    if n == 2 or n == 3:
        return n - 1
    if n % 3 == 0:
        return 3**(n/3)
    if n % 3 == 1:
        return 3**(n/3 - 1)*4
    if n % 3 == 2:
        return 3**(n/3)*2
