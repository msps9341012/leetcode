def bulbSwitch(n):
    """
    :type n: int
    :rtype: int
    """
    b=[1]*n
    for i in range(1,n):
        for j in range(n//(i+1)):
        	b[i+(i+1)*j]=b[i+(i+1)*j]^1
    return sum(b)

def bulbSwitch(n):
	a = [0]*(n+1)
	a = numpy.array(a)
	for i in xrange(1,n+1):
	    a[::i] = 1-a[::i] 
	return sum(a[1:])


def bulbSwitch2(n):
	i=1
	count=0
	while i*i<=n:
		count=count+1
		i=i+1
	return count
print(bulbSwitch2(9))