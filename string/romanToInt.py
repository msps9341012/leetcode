def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    romanNum = {"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
    res=0
    i=0
    while i<len(s):
        if s[i:i+2] in romanNum:
            res=res+romanNum[s[i:i+2]]
            i=i+2
        else:
            res=res+romanNum[s[i]]
            i=i+1
    return res
        
print(romanToInt("IX"))