def superPow(a, b):
    """
    :type a: int
    :type b: List[int]
    :rtype: int
    """
    if a%1337==0:
        return 0
    table=[]
    i=1
    while a**i%1337 not in table:
        table.append(a**i%1337)
        i=i+1
    res=0
    for i in b:
        res=res*10+i
    print(res)
    return (table[res%len(table)-1])

def superPow2(a, b):
    res = 1
    print(a)
    for n in b[::-1]:
        res *= (a**n)%1337
        a = (a**10)%1337
        print(a)
    return res % 1337

superPow2(2,[1,2,3])