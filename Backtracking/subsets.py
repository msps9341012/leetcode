def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return [[]]
    res=[]
    for i in nums:
        tmp=[]
        for j in res:
            tmp.append(j+[i])
        res=res+tmp
        res.append([i])
    return res+[[]]

def subsets2(nums):
    res = [[]]
    for num in nums:
        res += [item+[num] for item in res]
    return res

#recursive
def subsets(self, nums):
    res = []
    self.dfs(nums, 0, [], res)
    return res

def dfs(self, nums, index, path, res):
    res.append(path)
    for i in xrange(index, len(nums)):
        self.dfs(nums, i+1, path+[nums[i]], res)



print(subsets2([1,2,3]))