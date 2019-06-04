def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0

    for k in range(len(haystack)):
        i=k
        j=0
        while i<len(haystack):
            if haystack[i]!=needle[j]:
                break
            else:
                i=i+1
                j=j+1
                if j==len(needle):
                    return k
    return -1

print(strStr('aaaaa','bba'))