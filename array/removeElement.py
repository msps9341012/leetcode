class Solution(object):
    def bf_removeElement(self, nums, val):
        count=0
        for i in nums:
            if i==val:
                count=count+1
        i=0
        j=len(nums)-1
            
        while(i<j):
            if nums[i]==val and nums[j]!=val:
                #swap
                tmp=nums[i]
                nums[i]=nums[j]
                nums[j]=tmp
                i=i+1
                j=j-1
            if nums[j]==val:
                j=j-1
            if nums[i]!=val:
                i=i+1
        return len(nums)-count

    def removeElement(self, nums, val):
        #two pointer
        #just copy the value and increase the index
        count = 0 
        for i in range(len(nums)):
            if nums[i] != val :
                nums[count] = nums[i]
                count +=1
        return count

