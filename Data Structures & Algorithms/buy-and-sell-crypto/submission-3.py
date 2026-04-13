class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        if len(prices) == 1:
            return 0
        res = 0
        while left < len(prices) and right < len(prices):
            profit = prices[right] - prices[left]
            res = max(res, profit)
            if prices[left] > prices[right]:
                left = right
            right += 1
        return res
