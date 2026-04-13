class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 1
        dp = [0] * (target+1)
        for i in range(1,target+1):
            for num in nums:
                if num > i:
                    continue
                elif num == i:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-num]
        return dp[-1]