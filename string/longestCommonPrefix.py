class Solution(object):
    def longestCommonPrefix(self, strs):
        
        def commonPrefix(word1, word2):
            end = min(len(word1),len(word2))
            if(word1[0]!=word2[0]):
                return ''      
            for i in range(1,end):
                if(word1[i]!=word2[i]):
                    return word1[:i]
            return word1[:end]
            
        if not strs:
            return ''   
        if(len(strs) == 1):
            return strs[0]
        
        commPre = strs[0]
        
        for string in (strs[1:]):  
            if(string == '' or commPre == ''):
                return ''     
            commPre = commonPrefix(commPre,string) 
        return commPre