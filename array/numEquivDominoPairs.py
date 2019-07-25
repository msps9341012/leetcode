def numEquivDominoPairs(self,dominoes):
    """
    tuple 可以當dict 的key
    """
	s, D = 0, {}
	for d in dominoes:
		x = tuple(sorted(d))
		if x in D:
			D[x] += 1
		else:
			D[x] = 0
	return sum([i*(i+1)//2 for i in list(D.values())])

dominoes = [[1,2],[2,1],[3,4],[5,6]]

print(numEquivDominoPairs(dominoes))