def hammingWeight(n):
	bit=1<<32
	count=0
	while bit:
		if bit&n:
			count=count+1
		bit=bit>>1
	return count


def hammingWeight(self, n):
    """
	n & (n-1) which converts n into n with it's lowest set bit erased. 
	e.g. x = 1101
	x = x & (x-1)
	x = 1100

    """
    result = 0
    while n:
        result += 1 #只要不是等於零就一定會有一個
        n = n & (n-1)
    return result