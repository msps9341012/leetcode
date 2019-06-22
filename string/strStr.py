'''
重點是search needle的size 就好
不用全部跑完haystack的size
'''
def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0

    for i in range(len(haystack)-len(needle)+1):
        if (haystack[i:i + len(needle)] == needle):
            return i

    return -1

def strStr(self, haystack, needle):
    l1, l2 = len(haystack), len(needle)
    for i in xrange(l1 - l2 + 1):
        j = 0
        while j < l2 and needle[j] == haystack[i+j]:
            j += 1
        if j == l2:
            return i
    return -1
