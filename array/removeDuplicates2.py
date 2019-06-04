class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        index = 2
        for i in range(2, len(nums)):
            if (nums[i] != nums[index-2]):
                nums[index] = nums[i]
                index=index+1
        return index

    def removeDuplicates(self, nums):
        """
        cur紀錄要更換的位置
        超過兩個相同時cur不動 直到遇到下一個不同的
        """
        if len(nums)==0:
            return 0
        cur=1
        sum=0
        for i in range(1,len(nums)):
            temp=nums[i]
            if(nums[i]==nums[i-1]):
                sum=sum+1
                if sum<2:  
                    nums[cur]=temp
                    cur=cur+1
            else:
                sum=0
                nums[cur]=temp
                cur=cur+1
        return cur
