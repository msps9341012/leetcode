def maxProduct(words):
    """
    :type words: List[str]
    :rtype: int
    """
    
    max_ans=0
    a={}
    for i in range(len(words)):
        a[i]=set(words[i])
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if len(a[i]-a[j])==len(a[i]):
                max_ans=max(len(words[i])*len(words[j]),max_ans)
    return max_ans




def maxProduct2(words):
    d = {}
    for w in words:
        mask = 0
        for c in set(w):
            mask |= (1 << (ord(c) - 97)) #也就是 a:0001 b:0010 ab:0011 etc
        d[mask] = max(d.get(mask, 0), len(w)) #key 為binary represenation value 為length
    max_len=0
    for i in d:
        for j in d:
            if not i&j:
                max_len=max(d[i]*d[j],max_len)
    return max_len
