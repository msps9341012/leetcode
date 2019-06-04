class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a=[None]*len(nums)
        for i in range(len(nums)):
            a[(i + k) % len(nums)] = nums[i];
        for i in range(len(nums)):
            nums[i] = a[i]
    
    def rotate(nums, k):

        for i in range(k):
            previous=nums[-1]
            for j in range(len(nums)):
                temp = nums[j];
                nums[j] = previous;
                previous = temp;
        print(nums)
    def reverse(nums,i,j):
        while i<j:
            tmp=nums[j]
            nums[j]=nums[i]
            nums[i]=tmp
            i=i+1
            j=j-1
    def rotate(nums,k):
        k = k % len(nums)
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)




def rotate2(nums, k):

    def swap(i,j):
        tmp=nums[i]
        nums[i]=nums[j]
        nums[j]=tmp
    k=k % len(nums)
    index=0
    for i in range(len(nums)-k,len(nums)):
        for j in range(i,index,-1):
            swap(j,j-1)
        index=index+1
    print(nums)
rotate2([1,2],3)