def divide(dividend, divisor):

    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        shift=0
        while dividend>=divisor<<shift:
            shift=shift+1
        res=res+(1<<(shift-1))
        dividend=dividend-(divisor<<(shift-1))
    if not positive:
        res = -res
    return min(max(-2147483648, res), 2147483647)
print(divide(32,3))

    '''
    i=i+i 會比i<<1 快
    將divisor*2 與dividend比
    32/3 6 12 24 48則跳出
    32-24=8
    1+2+4
    8/3 6 9跳出
    '''