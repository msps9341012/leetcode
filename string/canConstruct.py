class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        if ransomNote==magazine:
            return True
        from collections import Counter
        c=Counter(magazine)
        for i in ransomNote:
            if i not in c or c[i]==0:
                return False
            else:
                c[i]=c[i]-1
        return True

        return all(ransomNote.count(c)<=magazine.count(c) for c in string.ascii_lowercase)