def singleNumber(nums):
    """
    先找出唯一的兩個數的xor的值
    從該值找出不同的bit(mask)
    從那個mask對list切成兩組
    再分別作xor即可
    """
    xor = 0
    a = 0
    b = 0
    for num in nums:
        xor ^= num
    mask = 1
    while(xor&mask == 0): 
        mask = mask << 1
    for num in nums:
        if num&mask:
        	a ^= num
        else:
        	print(num)
        	b ^= num
    return [a, b]


singleNumber([1,4,1,3,4,5])

