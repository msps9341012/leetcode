def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
    	return [[]]
    nums.sort()
    res=[]
    for i in nums:
        for j in range(len(res)):
        	if res[j]+[i] not in res:
        		res.append(res[j]+[i])
        if [i] not in res:
        	res.append([i])
    return res+[[]]

'''
遇到重複的num 就跳過從上一次的尾開始
[] 1 2 12 22 122
222 1222
'''
def subsetsWithDup2(nums):
    nums, result, pos = sorted(nums), [[]], {}
    for n in nums:
        start, l = pos.get(n, 0), len(result)
        result += [r + [n] for r in result[start:]]
        pos[n] = l
        print(n,start,result,l,pos)
    return result

def subsetsWithDup(self, S):
    res = [[]]
    S.sort()
    for i in range(len(S)):
        if i == 0 or S[i] != S[i - 1]:
            l = len(res)
        for j in range(len(res) - l, len(res)):
            res.append(res[j] + [S[i]])
    return res

print(subsetsWithDup2([1,2,2,3]))