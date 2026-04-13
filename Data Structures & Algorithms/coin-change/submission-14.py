class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0] + [-1] * amount 
        for i in range(amount+1):
                if i < min(coins):
                     continue
                for j in coins:
                    if i < j or dp[i-j] == -1:
                        continue
                    else:
                        if dp[i] == -1:
                            dp[i] = dp[i - j]    
                        else:
                            dp[i] = min(dp[i], dp[i-j])
                if dp[i] != -1:
                    dp[i] += 1
        return dp[-1]


