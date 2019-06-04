class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return -1
        dup_dict={}
        for i in range(len(s)):
            if s[i] not in dup_dict:
                dup_dict[s[i]]=1
            else:
                dup_dict[s[i]]=dup_dict[s[i]]+1
        index=0
        for i in s:
            if dup_dict[i]==1:
                return index
            else:
                index=index+1
        return -1
    def firstUniqChar(self, s):
        """
        list比dict快
        """
        counts = [0] * 26
        for item in s:
            counts[ord(item) - ord('a')] += 1
        for (index, item) in enumerate(s):
            if counts[ord(item) - ord('a')] == 1:
                return index
        return -1