class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dps = {}
        def dp(i,buying):
            if i >= len(prices):
                return 0
            if (i,buying) in dps:
                return dps[(i,buying)]
            cooldown = dp(i+1,buying)
            if buying:
                buy = dp(i+1, not buying) - prices[i]
                dps[(i,buying)] = max(buy,cooldown)
            else:
                sell = dp(i+2, not buying) + prices[i]
                dps[(i,buying)] = max(sell,cooldown)
            return dps[(i,buying)]
        return dp(0,True)
            

        