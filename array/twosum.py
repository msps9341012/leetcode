class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={}
        for i, num in enumerate(nums):
            n=target-num
            if n not in dict:
                dict[num]=i
            else:
                return [dict[n],i]