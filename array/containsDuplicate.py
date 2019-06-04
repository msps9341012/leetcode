def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dict={}
    for i in nums:
        if i not in dict:
            dict[i]=1
        else:
            return True
    return False

