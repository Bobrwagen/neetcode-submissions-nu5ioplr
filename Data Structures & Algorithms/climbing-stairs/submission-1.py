class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [1] + [0] * (n - 1)
        for i in range(1,n):
            dp[i] += dp[i-1]
            if i > 1:
                dp[i] += dp[i-2]
        
        return dp[-1] + dp[-2]

        