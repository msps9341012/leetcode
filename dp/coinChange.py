'''
bottom up/ top down
'''
def coinChange(self, coins, amount):
    MAX = float('inf')
    dp = [0] + [MAX] * amount

    for i in xrange(1, amount + 1):
        dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

    return [dp[amount], -1][dp[amount] == MAX]


def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = [0] + [float('inf')] * amount
    
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    
    return dp[-1] if dp[-1] != float('inf') else -1