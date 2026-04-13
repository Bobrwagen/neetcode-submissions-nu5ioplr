class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(n):
            dp_new = defaultdict(int)
            for total, count in dp.items():
                dp_new[total + nums[i]] += count
                dp_new[total - nums[i]] += count
            dp = dp_new
        return dp[target]
            
        