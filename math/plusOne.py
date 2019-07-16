def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    if (digits[-1]+1)!=10:
        digits[-1]=digits[-1]+1
        return digits
    else:
        carry=1
        i=-1
        while i>-1*len(digits)-1:
            if (digits[i]+1)==10:
                digits[i]=0
            else:
                digits[i]=digits[i]+1
                carry=0
                break
            i=i-1
    if carry:
        digits=[carry]+digits
    return digits
print(plusOne([9,9,9,9]))