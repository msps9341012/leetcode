'''
概念就是想辦法生出key (唯一性)
可以用count或是用sort的順序
'''

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    res=[[strs[0]]]
    for i in strs[1:]:
        flag=0
        for j in res:
            if checkpermutation(j[0],i):
                j.append(i)
                flag=1
        if flag==0:
            res.append([i])
    print(res)

def checkpermutation(string1, string2):
    if len(string1)==len(string2):
        vol={}
        for i in string1:
            if i in vol:
                vol[i]=vol[i]+1
            else:
                vol[i]=1
        for i in string2:
            if i not in vol:
                return False
            vol[i]=vol[i]-1
            if vol[i]==0:
                del vol[i]
        return len(vol)==0
    else:
        return False 

def groupAnagrams2(strs):
    ans = {}
    for s in strs:
        key=tuple(sorted(s))
        if key in ans:
            ans[key].append(s)
        else:
            ans[key]=[s]
    return ans.values()

print(groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))