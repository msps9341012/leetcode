def isPalindrome(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i].lower()!=s[j].lower():
            if s[i].isalnum() and s[j].isalnum():
                return False
            if not s[i].isalnum():
                i=i+1
            if not s[j].isalnum():
                j=j-1
        else:
            i=i+1
            j=j-1
    return True


print(isPalindrome("OP"))