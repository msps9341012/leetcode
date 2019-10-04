#O(mn)
def calculateMinimumHP1(dungeon):
    if not dungeon:
        return 
    r, c = len(dungeon), len(dungeon[0])
    dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
    dp[-1][-1] = max(1, 1-dungeon[-1][-1])
    
    for i in xrange(c-2, -1, -1):
        dp[-1][i] = max(1, dp[-1][i+1]-dungeon[-1][i])
    for i in xrange(r-2, -1, -1):
        dp[i][-1] = max(1, dp[i+1][-1]-dungeon[i][-1])
    for i in xrange(r-2, -1, -1):
        for j in xrange(c-2, -1, -1):
            dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
    return dp[0][0]


#O(n)
def calculateMinimumHP(self, dungeon):
    """
    :type dungeon: List[List[int]]
    :rtype: int
    """
    if not dungeon:
        return 
    r, c = len(dungeon), len(dungeon[0])
    dp = [0 for _ in xrange(c)]
    dp[-1] = max(1, 1-dungeon[-1][-1])
    for i in xrange(c-2, -1, -1):
        dp[i] = max(1, dp[i+1]-dungeon[-1][i])
    for i in xrange(r-2, -1, -1):
        dp[-1] = max(1, dp[-1]-dungeon[i][-1])
        for j in xrange(c-2, -1, -1):
            dp[j] = max(1, min(dp[j], dp[j+1])-dungeon[i][j])
    return dp[0]

x=[[1,-3,3],
[0,-2,0],
[-3,3,5]]

print(calculateMinimumHP1(x))