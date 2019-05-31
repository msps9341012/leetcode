class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        for t in range(len(nums)-2):
            if nums[t]+nums[t+1]+nums[t+2]>0:
                break
            if nums[t]+nums[-2]+nums[-1]<0:
                continue 
            if t>0 and nums[t]==nums[t-1]:
                continue
            i=t+1
            j=len(nums)-1
            while (i<j):
                sum_=nums[t]+nums[i]+nums[j]
                if (sum_==0):
                    res.append([nums[t],nums[i],nums[j]])
                    i=i+1
                    j=j-1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif sum_<0:
                    i=i+1
                elif sum_>0:
                    j=j-1
        return res
