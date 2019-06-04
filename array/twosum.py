class Solution(object):
    def twoSum(self, nums, target):
        """
        如果序列已排序 可用two pointer去解
        """
        dict={}
        for i, num in enumerate(nums):
            n=target-num
            if n not in dict:
                dict[num]=i
            else:
                return [dict[n],i]
