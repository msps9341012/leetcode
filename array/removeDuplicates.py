def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    '''
    dict={}
    count=0
    i=0
    j=len(nums)-1
    while (i<j):
        if nums[i] in dict:
            if nums[j] not in dict:
                dict[nums[j]]=True
                nums[i]=nums[j]
                i=i+1
            else:
                count=count+1
            j=j-1
            count=count+1
        if nums[i] not in dict:
            dict[nums[i]]=True
            i=i+1
    print(nums,count)
    '''
    #抓間隔就好拉
    len_ = 0
    if len(nums)==0:
        return 0
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            len_ +=1
            nums[len_] = nums[i]
    print(nums)
    return len_
removeDuplicates( [0,1,1,2])