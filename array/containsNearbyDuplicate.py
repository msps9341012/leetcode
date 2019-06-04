class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                tmp=i-dict[nums[i]]
                if tmp<=k:
                        return True
                dict[nums[i]]=i
            else:
                dict[nums[i]]=i
        return False