def longestPalindromeSubseq(self, s):
    if s == s[::-1]:
        return len(s)
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))] 
    for i in range(len(s)-1,-1,-1): 
        for j in range(i,len(s)): 
            if i == j: 
                dp[i][j] =1 
            elif s[i] == s[j]: 
                dp[i][j] = dp[i+1][j-1]+2 
            else: 
                dp[i][j] = max(dp[i][j-1], dp[i+1][j]) 
    return dp[0][len(s)-1]